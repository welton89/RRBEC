from django.shortcuts import render, redirect

from comandas.models import Comanda, ProductComanda
from products.models import Product


def listProduct(request, comanda_id):
    product = request.GET.get("search-product")
    products = Product.objects.filter(name__icontains=product)
    return render(request, "htmx_components/htmx_list_products.html", {"products": products,'comanda_id':comanda_id})

def addProduct(request, product_id, comanda_id):
    product_comanda = ProductComanda(comanda_id=comanda_id, product_id=product_id)
    product_comanda.save()
    consumo = ProductComanda.objects.filter(comanda=comanda_id)
    total = 0
    for produto in consumo:
        total += produto.product.price
    return render(request, "htmx_components/htmx_list_products_in_comanda.html",{'consumo': consumo, 'total': total})


def removeProductComanda(request, productComanda_id):
    product_comanda = ProductComanda.objects.get(id=productComanda_id)
    consumo = ProductComanda.objects.filter(comanda=product_comanda.comanda)
    product_comanda.delete()
    total = 0
    for produto in consumo:
        total += produto.product.price
    return render(request, "htmx_components/htmx_list_products_in_comanda.html",{'consumo': consumo, 'total': total})

def closeComanda(request, comanda_id):
    # id = request.POST.get('id-comanda')
    # comanda_id = int(id)
    comanda = Comanda.objects.get(id=comanda_id)
    comanda.status = "PAYING"
    comanda.save()
    return redirect('comandas')