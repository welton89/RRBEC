from datetime import date
from decimal import Decimal
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


from comandas.models import Comanda, ProductComanda, StockMovementType, StockMovement
from orders.models import Order
from products.models import Product
from payments.models import Payments, somar
from typePay.models import TypePay
from gestaoRaul.decorators import group_required
from websocket_client.websocketClient import enviar_mensagem

from asgiref.sync import async_to_sync
# import asyncio

# import websockets

# async def enviar_mensagem(msg):
#     try:
#         uri = "ws://websocket_server:8765"
#         async with websockets.connect(uri) as websocket:
#             await websocket.send(msg)
#             # print(f"> Enviado: {msg}")

#             # resposta = await websocket.recv()
#             # print(f"< Recebido: {resposta}")
#     except Exception as e:
#         print(f"Erro ao enviar mensagem via websocket: {e}")




@group_required(groupName='Garçom')
def removeProductComanda(request, productComanda_id):
    config = {
        'taxa': False
        }
    product_comanda = ProductComanda.objects.get(id=productComanda_id)
    comanda = product_comanda.comanda
    product = product_comanda.product
    user = User.objects.get(id=request.user.id)
    typeMovement = StockMovementType.objects.get(name="Estorno")

    if comanda.status == 'OPEN':
        parcial = Payments.objects.filter(comanda=comanda)
        consumo = ProductComanda.objects.filter(comanda=comanda)
        valores = somar(consumo,comanda)
        if product_comanda.product.cuisine == True:
            order = Order.objects.get(productComanda=product_comanda)

            StockMovement.sumTransactionStock(
                    product=product,
                    movement_type=typeMovement,
                    comanda=comanda,
                    user=user,
                    qtd=1,
                    obs= "Excluido da comanda"
                )
            product_comanda.delete()

            msg = JsonResponse({
                'type': 'broadcast',
                'message': 'Atenção! Pedido cancelado', 
                'local':'cozinha',
                    'tipo':'delete',
                    'id':order.id,
                    'speak': f'Pedido cancelado!  {order.id_product.name}.'
                    }) 
            # asyncio.run(enviar_mensagem(msg))
            # order.delete()
            consumo = ProductComanda.objects.filter(comanda=comanda)
            valores = somar(consumo,comanda)
        else:
            StockMovement.sumTransactionStock(
                    product=product,
                    movement_type=typeMovement,
                    comanda=comanda,
                    user=user,
                    qtd=1,
                    obs= "Excluido da comanda"
                )
            product_comanda.delete()
            consumo = ProductComanda.objects.filter(comanda=comanda)
            valores = somar(consumo,comanda)

        return render(request,
            "htmx_components/comandas/htmx_list_products_in_comanda.html",
            {'config':config,
            'valores': valores,
            'parcials':parcial,
            'consumo': consumo, 
            'comanda':comanda})
    else:
        pass



@group_required(groupName='Gerente')
def reopenComanda(request, comanda_id):
    comanda = Comanda.objects.get(id=comanda_id)
    if comanda.status == 'CLOSED':
        pass
    else:
        comanda.status = "OPEN"
        comanda.save()

@group_required(groupName='Gerente')
def paymentComanda(request, comanda_id):
    taxa = request.POST.get('taxa',False)
    typePayment = TypePay.objects.get(id=1)
    consumo = ProductComanda.objects.filter(comanda=comanda_id)
    comanda = Comanda.objects.get(id=comanda_id)
    valores = somar(consumo,comanda)
    if taxa == 'True':
        pagamento = Payments(value=valores['totalComTaxa'], comanda=comanda, type_pay=typePayment,description='tipo de pagamento mokado')
        pagamento.save()
    else:
        pagamento = Payments(value=valores['totalSemTaxa'], comanda=comanda, type_pay=typePayment,description='tipo de pagamento mokado')
        pagamento.save()

    comanda.status = 'CLOSED'
    comanda.save()
    return redirect('/comandas')

@group_required(groupName='Gerente')
def paymentParcial(request, comanda_id):
    typePayment = TypePay.objects.get(id=1)
    comanda = Comanda.objects.get(id=comanda_id)
    value = Decimal(request.POST.get('value-parcial'))
    description = request.POST.get('name-parcial')
    pagamento = Payments(value=value, comanda=comanda, type_pay=typePayment,description=description)
    pagamento.save()
    return redirect('/comandas')
