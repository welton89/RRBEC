# from datetime import timezone
from django.utils import timezone
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


from orders.models import Order
from django.db.models import Q
from gestaoRaul.decorators import group_required


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
    return  render(request, 'htmx_components/orders/htmx_list_orders_fila.html',{'orders': orders})


@group_required(groupName='Cozinha')
def finished(request, order_id):
    order = Order.objects.get(id=order_id)
    order.finished = timezone.now()
    order.save()
    fifteen_hours_ago = timezone.now() - timezone.timedelta(hours=15)
    orders = Order.objects.filter(queue__gte=fifteen_hours_ago )
    return  render(request, 'htmx_components/orders/htmx_list_orders_fila.html',{'orders': orders})

@group_required(groupName='Garçom')
def delivered(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delivered = timezone.now()
    order.save()
    fifteen_hours_ago = timezone.now() - timezone.timedelta(hours=15)
    orders = Order.objects.filter(queue__gte=fifteen_hours_ago )
    return  render(request, 'htmx_components/orders/htmx_list_orders_fila.html',{'orders': orders})


def notificacao(request):
    fifteen_hours_ago = timezone.now() - timezone.timedelta(hours=15)
    ordersFila = Order.objects.filter(queue__gte=fifteen_hours_ago)
    ordersPronto = Order.objects.filter(queue__gte=fifteen_hours_ago, finished__isnull=False)
    print(len(ordersFila))
    print(len(ordersPronto))

    grupoCozinha = request.user.groups.filter(name='Cozinha').exists()
    grupoGarcom = request.user.groups.filter(name='Garçom').exists()
    grupoGerente = request.user.groups.filter(name='Gerente').exists()

    if grupoCozinha == True:
        if 'fila' in request.COOKIES:
            cookiesFila = int(request.COOKIES['fila'])
            if len(ordersFila) > cookiesFila:
                return JsonResponse({
                        'notificacao': 'true',
                        'fila': len(ordersFila),
                         'pronto':len(ordersPronto),
                        'titulo': 'Pedido para: '+ ordersFila[len(ordersFila)-1].id_comanda.name,
                        'corpo': ordersFila[len(ordersFila)-1].id_product.name,
                    })
            else:
                return JsonResponse({
                        'notificacao': 'false',
                        'fila': len(ordersFila),
                         'pronto':len(ordersPronto),
                    })
        else:
            return JsonResponse({
            'notificacao': 'true',
            'fila': len(ordersFila),
             'pronto':len(ordersPronto),
            'titulo': 'Pedido para: '+ ordersFila[len(ordersFila)-1].id_comanda.name,
            'corpo': ordersFila[len(ordersFila)-1].id_product.name,
        })

    elif grupoGarcom == True and grupoGerente == False:

        if 'pronto' in request.COOKIES:
            cookiesPronto = int(request.COOKIES['pronto'])
            if len(ordersPronto) > cookiesPronto:
                return JsonResponse({
                        'notificacao': 'true',
                        'fila': len(ordersPronto),
                         'pronto':len(ordersPronto),
                        'titulo': ordersPronto[len(ordersPronto)-1].id_comanda.name,
                        'corpo': ordersPronto[len(ordersPronto)-1].id_product.name,
                    })
            else:
                return JsonResponse({
                        'notificacao': 'false',
                        'fila': len(ordersPronto),
                    })
        else:
            return JsonResponse({
            'notificacao': 'false',
            'fila': len(ordersPronto),
            'pronto':len(ordersPronto),
            'titulo': ordersPronto[len(ordersPronto)-1].id_comanda.name,
            'corpo': ordersPronto[len(ordersPronto)-1].id_product.name,
             })


    else:
        return JsonResponse({
            'notificacao': 'false',
            'fila': len(ordersPronto),
            'pronto':len(ordersPronto),
            'titulo': ordersPronto[len(ordersPronto)-1].id_comanda.name,
            'corpo': ordersPronto[len(ordersPronto)-1].id_product.name,
             })

    