from django.shortcuts import render, redirect

from categories.models import Categories
from products.models import Product


def products(request):
    protucts = Product.objects.all()
    categories = Categories.objects.all()
    return render(request, 'products.html', {'products': protucts, 'categories': categories})


def createProduct(request):
    print(request.POST)
    name = request.POST.get('name')
    description = request.POST.get('description')
    price = request.POST.get('price')
    category = request.POST.get('category')
    product = Product(name=name, description=description, price=price, category=category)
    product.save()
    return redirect('/products')
    # return render(request, 'products.html')