from django.shortcuts import render, redirect

from categories.models import Categories
from products.models import Product
from gestaoRaul.decorators import group_required



@group_required(groupName='Garçom')
def products(request):
    protucts = Product.objects.all()
    categories = Categories.objects.all()
    # teste = Product.objects.get(id=389)
    # teste.image = "https://ehgomes.com.br/wp-content/uploads/2023/08/Vectorizer.AI-A-Ferramenta-que-Transforma-Imagens-em-Vetores.webp"
    # teste.save()
    # print((teste.image))
    return render(request, 'products.html', {'products': protucts, 'categories': categories})

@group_required(groupName='Garçom')
def searchProduct(request):
    product = request.GET.get("search-product")
    products = Product.objects.filter(name__icontains=product)
    return render(request, "htmx_components/products/htmx_search_products.html", {"products": products})


@group_required(groupName='Gerente')
def createProduct(request):
    name = request.POST.get('name')
    description = request.POST.get('description')
    price = request.POST.get('price')
    category = Categories.objects.get(id = int(request.POST.get('select-categorie')))
    product = Product(name=name, description=description, price=price, category=category)
    product.save()
    return redirect('/products')



@group_required(groupName='Gerente')
def onOffProduct(request):
    id = request.POST.get('id-product')
    product_id = int(id)
    product = Product.objects.get(id=product_id)
    product.active = not product.active
    product.save()
    products = Product.objects.all()
    return render(request, "htmx_components/products/htmx_search_products.html", {"products": products})


@group_required(groupName='Gerente')
def editProduct(request, productId):
    product_id = int(request.POST.get('productId'))
    # product_id = productId
    product = Product.objects.get(id=product_id)
    product.name = request.POST.get('name')
    product.description = request.POST.get('description')
    product.price = request.POST.get('price')
    product.quantity = request.POST.get('qtd')
    product.image = request.POST.get('image')
    product.cuisine = True if request.POST.get('cuisine') else False
    product.category = Categories.objects.get(id = int(request.POST.get('select-categorie')))
    product.save()
    product = request.GET.get("search-product")
    if product == None:
        product = ''
    products = Product.objects.filter(name__icontains=product)
    return render(request, "htmx_components/products/htmx_search_products.html", {"products": products})
