from django.shortcuts import render, redirect

from comandas.models import Comanda, ProductComanda
from products.models import Product


def listProduct(request):
    product = request.GET.get("search-product")
    products = Product.objects.filter(name__icontains=product)
    return render(request, "htmx_components/htmx_list_products.html", {"products": products})

def addProduct(request, product_id, comanda_id):
    product_comanda = ProductComanda(comanda_id=comanda_id, product_id=product_id)
    product_comanda.save()
    return render(request, "htmx_components/htmx_add_product.html",)