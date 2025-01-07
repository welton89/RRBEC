from django.shortcuts import render, redirect

from categories.models import Categories
from products.models import Product


def products(request):
    protucts = Product.objects.all()
    categories = Categories.objects.all()
    return render(request, 'products.html', {'products': protucts, 'categories': categories})

def searchProduct(request):
    product = request.GET.get("search-product")
    products = Product.objects.filter(name__icontains=product)
    return render(request, "htmx_components/products/htmx_search_products.html", {"products": products})


def createProduct(request):
    name = request.POST.get('name')
    description = request.POST.get('description')
    price = request.POST.get('price')
    category = Categories.objects.get(id = int(request.POST.get('select-categorie')))
    product = Product(name=name, description=description, price=price, category=category)
    product.save()
    return redirect('/products')
    # return render(request, 'products.html')


def onOffProduct(request):
    id = request.POST.get('id-product')
    product_id = int(id)
    product = Product.objects.get(id=product_id)
    product.active = not product.active
    product.save()
    return redirect('products')

def editProduct(request, productId):
    # id = request.POST.get('productId')
    product_id = productId
    product = Product.objects.get(id=product_id)
    product.name = request.POST.get('name')
    product.description = request.POST.get('description')
    product.price = request.POST.get('price')
    product.quantity = request.POST.get('qtd')
    product.category = Categories.objects.get(id = int(request.POST.get('select-categorie')))
    product.save()
    return redirect('products')