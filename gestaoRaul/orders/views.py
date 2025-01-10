from django.shortcuts import render

from orders.models import Order

def viewsOrders(request):
    orders = Order.objects.all()
    o = orders[0].id_comanda
    return  render(request, 'orders.html',{'orders': orders})
