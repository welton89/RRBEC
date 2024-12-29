from django.shortcuts import render, redirect

from comandas.models import Comanda, ProductComanda
from products.models import Product
from django.db.models import Count, F



def viewBalcao(request):

    comanda = Comanda.objects.get(name='VENDA BALCÃO')
    consumo = ProductComanda.objects.filter(comanda=comanda.id)
    produtos_mais_vendidos = list(ProductComanda.objects.values('product').annotate(
    quantidade=Count('product'),
    nome=F('product__name') ).order_by('-quantidade'))
    products = Product.objects.all()
    products_ordenados = []

    for produto in produtos_mais_vendidos:
        for p in products:
            if p.name == produto['nome']:
                products_ordenados.append(p)

    total = 0
    for produto in consumo:
        total += produto.product.price
  
    return render(request, 'viewBalcao.html', {'comanda': comanda, 'consumo': consumo, 'total': total, 'products': products_ordenados})


