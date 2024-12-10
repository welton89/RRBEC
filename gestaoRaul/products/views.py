from django.shortcuts import render

from products.models import Product


def products(request):
    protucts = Product.objects.all()
    return render(request, 'products.html', {'products': protucts})