# from datetime import timezone
from django.utils import timezone
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
import asyncio
import websockets


from orders.models import Order
from django.db.models import Q
from gestaoRaul.decorators import group_required


async def enviar_mensagem(message):
    uri = "ws://192.168.1.150:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send(message)
        print(f"> Enviado: {message}")

        resposta = await websocket.recv()
        print(f"< Recebido: {resposta}")




def viewsOrders(request):
    fifteen_hours_ago = timezone.now() - timezone.timedelta(hours=15)
    orders = Order.objects.filter(queue__gte=fifteen_hours_ago )
    return  render(request, 'orders.html',{'orders': orders})

@group_required(groupName='Cozinha')
def preparing(request, order_id):
    order = Order.objects.get(id=order_id)
    order.preparing = timezone.now()
    order.save()
    fifteen_hours_ago = timezone.now() - timezone.timedelta(hours=15)
    orders = Order.objects.filter(queue__gte=fifteen_hours_ago )
    return redirect(request.META.get('HTTP_REFERER', '/'))


@group_required(groupName='Cozinha')
def finished(request, order_id):
    order = Order.objects.get(id=order_id)
    order.finished = timezone.now()
    order.save()
    fifteen_hours_ago = timezone.now() - timezone.timedelta(hours=15)
    orders = Order.objects.filter(queue__gte=fifteen_hours_ago )
    # asyncio.run(enviar_mensagem())
    return redirect(request.META.get('HTTP_REFERER', '/'))

@group_required(groupName='Garçom')
def delivered(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delivered = timezone.now()
    order.save()
    fifteen_hours_ago = timezone.now() - timezone.timedelta(hours=15)
    orders = Order.objects.filter(queue__gte=fifteen_hours_ago )
    return redirect(request.META.get('HTTP_REFERER', '/'))


def notificacao(request):
    fifteen_hours_ago = timezone.now() - timezone.timedelta(hours=15)
    ordersFila = Order.objects.filter(queue__gte=fifteen_hours_ago)
    ordersPronto = Order.objects.filter(queue__gte=fifteen_hours_ago, finished__isnull=False)

    grupoCozinha = request.user.groups.filter(name='Cozinha').exists()
    grupoGerente = request.user.groups.filter(name='Gerente').exists()

    if grupoCozinha == True and grupoGerente == False:
        if 'fila' in request.COOKIES:
            cookiesFila = int(request.COOKIES['fila'])
            if len(ordersFila) > cookiesFila:
                return JsonResponse({
                        'notificacao': 'true',
                        'fila': len(ordersFila),
                        'titulo': 'Pedido para: '+ ordersFila[len(ordersFila)-1].id_comanda.name,
                        'corpo': ordersFila[len(ordersFila)-1].id_product.name,
                    })
            else:
                return JsonResponse({
                        'notificacao': 'false',
                        'fila': len(ordersFila),
                    })
        else:
            return JsonResponse({
            'notificacao': 'true',
            'fila': len(ordersFila),
            'titulo': 'Pedido para: '+ ordersFila[len(ordersFila)-1].id_comanda.name,
            'corpo': ordersFila[len(ordersFila)-1].id_product.name,
        })

   
    else:
        return JsonResponse({
            'notificacao': 'false',
            'fila': len(ordersFila),
             })

    