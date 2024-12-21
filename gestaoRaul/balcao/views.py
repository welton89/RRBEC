from django.shortcuts import render, redirect

from comandas.models import Comanda, ProductComanda
from products.models import Product
from mesas.models import Mesa


# def balcao(request):
#     comandas = Comanda.objects.filter(status__in=["OPEN", "PAYING"])
#     mesas = Mesa.objects.all()
#     return render(request, 'comandas.html', {'comandas': comandas, 'mesas': mesas})



def viewBalcao(request):

    comanda = Comanda.objects.get(name='VENDA BALCÃO')
    consumo = ProductComanda.objects.filter(comanda=comanda.id)
    products = Product.objects.all()
    total = 0
    for produto in consumo:
        total += produto.product.price
  
    return render(request, 'viewBalcao.html', {'comanda': comanda, 'consumo': consumo, 'total': total, 'products': products})



# def createComanda(request):
#     name = request.POST.get('name-comanda')
#     mesa_id = int(request.POST.get('select-mesa')[0])
#     mesa = Mesa.objects.get(id=mesa_id)
#     comanda = Comanda(name=name, mesa=mesa)
#     comanda.save()

#     return redirect('comandas')

