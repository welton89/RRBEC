from django.shortcuts import render

from comandas.models import Comanda, ProductComanda
from products.models import Product
from mesas.models import Mesa
from django.db.models import Count, F
from django.contrib.auth.models import User
from gestaoRaul.decorators import group_required



@group_required(groupName='Garçom')
def viewBalcao(request):
    user = User.objects.get(id=request.user.id)
    try:
        comanda = Comanda.objects.get(name=f'{user.id} - BALCÃO - {user.first_name}')
    except:
        mesa = Mesa.objects.get(id=1)
        comanda = Comanda(name=f'{user.id} - BALCÃO - {user.first_name}', mesa=mesa, user=user,status='CLOSED')
        comanda.save()

    consumo = ProductComanda.objects.filter(comanda=comanda.id)
    products_ordenados = ProductComanda.maisVendidos()
    total = 0
    for produto in consumo:
        total += produto.product.price
  
    return render(request, 'viewBalcao.html', {'comanda': comanda, 'consumo': consumo, 'total': total, 'products': products_ordenados})


