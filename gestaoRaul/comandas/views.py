from django.shortcuts import render, redirect

from comandas.models import Comanda, ProductComanda
from products.models import Product
from mesas.models import Mesa


def comandas(request):
    comandas = Comanda.objects.filter(status__in=["OPEN", "PAYING"])
    mesas = Mesa.objects.all()
    return render(request, 'comandas.html', {'comandas': comandas, 'mesas': mesas})



def viewComanda(request):
    id = request.GET.get('parametro')
    comanda_id = int(id)
    comanda = Comanda.objects.get(id=comanda_id)
    consumo = ProductComanda.objects.filter(comanda=comanda_id)
    products = Product.objects.all()
    total = 0
    for produto in consumo:
        total += produto.product.price
  
    return render(request, 'viewcomanda.html', {'comanda': comanda, 'consumo': consumo, 'total': total, 'products': products})



def createComanda(request):
    name = request.POST.get('name-comanda')
    mesa_id = int(request.POST.get('select-mesa')[0])
    mesa = Mesa.objects.get(id=mesa_id)
    comanda = Comanda(name=name, mesa=mesa)
    comanda.save()

    return redirect('comandas')

