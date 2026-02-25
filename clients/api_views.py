from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Client
from .serializers import ClientSerializer
from comandas.models import Comanda, ProductComanda
from comandas.serializers import ComandaSerializer
from payments.models import Payments, somar
from typePay.models import TypePay

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Client.objects.all()

    @action(detail=True, methods=['get'])
    def fiados(self, request, pk=None):
        client = self.get_object()
        comandas = Comanda.objects.filter(client=client, status='FIADO')
        serializer = ComandaSerializer(comandas, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def pagar_fiados(self, request):
        comanda_ids = request.data.get('ids', [])
        if not comanda_ids:
            return Response({'error': 'Nenhum ID de comanda fornecido.'}, status=status.HTTP_400_BAD_REQUEST)
        
        results = []
        for comanda_id in comanda_ids:
            try:
                comanda = Comanda.objects.get(id=comanda_id)
                
                # Apenas processar se estiver como FIADO
                if comanda.status != 'FIADO':
                    results.append({'id': comanda_id, 'status': 'erro', 'message': 'Status da comanda não é FIADO.'})
                    continue

                # 1. Fechar a comanda
                comanda.status = 'CLOSED'
                comanda.save()

                # 2. Gerar o pagamento (Inspirado no payDebt original)
                try:
                    type_pay = TypePay.objects.get(id=1) # Assume ID 1 como padrão para recebimento de fiado
                except TypePay.DoesNotExist:
                    type_pay, _ = TypePay.objects.get_or_create(id=1, defaults={'name': 'Dinheiro'})

                consumo = ProductComanda.objects.filter(comanda=comanda)
                valores = somar(consumo, comanda)
                
                payment = Payments.objects.create(
                    value=valores['totalSemTaxa'], # Valor que falta pagar
                    type_pay=type_pay,
                    comanda=comanda,
                    client=comanda.client,
                    description='PAGAMENTO DE FIADO (via API)'
                )
                
                results.append({'id': comanda_id, 'status': 'sucesso', 'payment_id': payment.id})
                
            except Comanda.DoesNotExist:
                results.append({'id': comanda_id, 'status': 'erro', 'message': 'Comanda não encontrada.'})
            except Exception as e:
                results.append({'id': comanda_id, 'status': 'erro', 'message': str(e)})

        return Response({
            'success': True,
            'message': f'{len(comanda_ids)} comandas processadas',
            'results': results
        }, status=status.HTTP_200_OK)
