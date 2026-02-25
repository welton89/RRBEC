from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import Comanda, ProductComanda, StockMovement, StockMovementType
from .serializers import ComandaSerializer, ProductComandaSerializer
from payments.models import Payments
from typePay.models import TypePay
from clients.models import Client

class ComandaViewSet(viewsets.ModelViewSet):
    queryset = Comanda.objects.all()
    serializer_class = ComandaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Comanda.objects.all()

    @action(detail=True, methods=['post'])
    def apagar(self, request, pk=None):
        comanda = self.get_object()
        
        # 1. Recuperar os itens para devolver ao estoque
        itens = ProductComanda.objects.filter(comanda=comanda)
        
        # Tipo de movimentação: Estorno/Cancelamento (ajustar conforme os tipos existentes)
        # Se não houver um tipo específico, podemos buscar um genérico ou usar o de Venda com sinal invertido via sumTransactionStock
        try:
            typeMovement = StockMovementType.objects.get(name="Estorno - Comanda Apagada")
        except StockMovementType.DoesNotExist:
            # Fallback para um tipo existente se o de estorno não existir
            typeMovement, _ = StockMovementType.objects.get_or_create(name="Ajuste de Estoque (Cancelamento)")

        for item in itens:
            StockMovement.sumTransactionStock(
                product=item.product,
                movement_type=typeMovement,
                comanda=comanda,
                user=request.user,
                qtd=1,
                obs=f"Estorno: Comanda {comanda.name} apagada/limpa via API"
            )

        # 2. Excluir os itens da comanda
        itens.delete()
        
        # 3. Mudar o status para CLOSED
        comanda.status = 'CLOSED'
        comanda.save()
        
    @action(detail=True, methods=['post'])
    def pagar(self, request, pk=None):
        comanda = self.get_object()
        
        # Dados do pagamento vindos no request
        value = request.data.get('value')
        type_pay_id = request.data.get('type_pay')
        client_id = request.data.get('client')
        description = request.data.get('description', f"Pagamento da comanda {comanda.name}")

        if not value or not type_pay_id:
            return Response(
                {'error': 'Campos "value" e "type_pay" são obrigatórios.'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            type_pay = TypePay.objects.get(id=type_pay_id)
        except TypePay.DoesNotExist:
            return Response({'error': 'Tipo de pagamento não encontrado.'}, status=status.HTTP_400_BAD_REQUEST)

        client = None
        if client_id:
            try:
                client = Client.objects.get(id=client_id)
            except Client.DoesNotExist:
                return Response({'error': 'Cliente não encontrado.'}, status=status.HTTP_400_BAD_REQUEST)

        # 1. Criar o registro de pagamento
        payment = Payments.objects.create(
            value=value,
            type_pay=type_pay,
            comanda=comanda,
            client=client,
            description=description
        )

        # 2. Fechar a comanda
        comanda.status = 'CLOSED'
        comanda.dt_close = timezone.now()
        comanda.save()

        return Response({
            'status': 'Pagamento registrado e comanda fechada com sucesso.',
            'payment_id': payment.id
        }, status=status.HTTP_200_OK)

class ProductComandaViewSet(viewsets.ModelViewSet):
    queryset = ProductComanda.objects.all()
    serializer_class = ProductComandaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Salva o item na comanda
        product_comanda = serializer.save()
        
        # Recupera os dados para a movimentação de estoque
        product = product_comanda.product
        comanda = product_comanda.comanda
        
        # Tipo de movimentação: Venda - Comanda (como na view original)
        try:
            typeMovement = StockMovementType.objects.get(name="Venda - Comanda")
        except StockMovementType.DoesNotExist:
            typeMovement, _ = StockMovementType.objects.get_or_create(name="Saída de Estoque (API)")

        StockMovement.subTransactionStock(
            product=product,
            movement_type=typeMovement,
            comanda=comanda,
            user=self.request.user,
            qtd=1,
            obs="Adicionado na comanda via API"
        )

        # 3. Criar Pedido (Order) automaticamente se for item de cozinha
        # (Lógica inspirada no addProduct original)
        if product.cuisine:
            from orders.models import Order
            Order.objects.create(
                id_comanda=comanda,
                id_product=product,
                productComanda=product_comanda,
                obs=self.request.data.get('obs', '')
            )

    def perform_update(self, serializer):
        instance = serializer.save()
        obs = self.request.data.get('obs')
        if obs is not None:
            order = instance.order_set.first()
            if order:
                order.obs = obs
                order.save()

    def perform_destroy(self, instance):
        # Recupera os dados antes de deletar
        product = instance.product
        comanda = instance.comanda
        
        # Tipo de movimentação: Estorno/Cancelamento
        try:
            typeMovement = StockMovementType.objects.get(name="Estorno - Item Removido")
        except StockMovementType.DoesNotExist:
            typeMovement, _ = StockMovementType.objects.get_or_create(name="Ajuste de Estoque (Cancelamento)")

        # Realiza a devolução ao estoque
        StockMovement.sumTransactionStock(
            product=product,
            movement_type=typeMovement,
            comanda=comanda,
            user=self.request.user,
            qtd=1,
            obs=f"Estorno: Item {product.name} removido da comanda {comanda.name} via API"
        )
        
        # Deleta o registro definitivamente
        instance.delete()
