from django.shortcuts import render

from comandas.models import Comanda, ProductComanda
from products.models import Product
from mesas.models import Mesa
from django.db.models import Count, F
from django.contrib.auth.models import User
from gestaoRaul.decorators import group_required



@group_required(groupName='Garçom')
def viewBalcao(request):
    try:
        comanda = Comanda.objects.get(name='VENDA BALCÃO')
    except:
        user = User.objects.get(id=request.user.id)
        mesa = Mesa.objects.get(id=1)
        comanda = Comanda(name='VENDA BALCÃO', mesa=mesa, user=user,status='CLOSED')
        comanda.save()

    consumo = ProductComanda.objects.filter(comanda=comanda.id)
    produtos_mais_vendidos = list(ProductComanda.objects.values('product').annotate(
    quantidade=Count('product'),
    nome=F('product__name') ).order_by('-quantidade'))
    products = Product.objects.all()
    products_ordenados = []

    for produto in produtos_mais_vendidos:
        for p in products:
            if p.name == produto['nome'] and p.active == True:
                products_ordenados.append(p)

    total = 0
    for produto in consumo:
        total += produto.product.price
  
    return render(request, 'viewBalcao.html', {'comanda': comanda, 'consumo': consumo, 'total': total, 'products': products_ordenados})


