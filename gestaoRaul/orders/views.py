# from datetime import timezone
from django.utils import timezone
from django.shortcuts import render

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
