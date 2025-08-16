from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from django.db.models import Q, Count, F


from categories.models import Categories
from comandas.models import ProductComanda
from products.models import Product
from gestaoRaul.decorators import group_required



@group_required(groupName='Garçom')
def products(request):
    protucts = Product.objects.all().order_by('-active', 'category') 
    categories = Categories.objects.all()
    return render(request, 'products.html', {'products': protucts, 'categories': categories})

@group_required(groupName='Garçom')
def searchProduct(request):
    product = request.GET.get("search-product")
    products = Product.objects.filter(name__icontains=product).order_by('-active', 'category') 
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
    products = Product.objects.all().order_by('-active', 'category') 
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

def createJson(request):
    produtos_mais_vendidos = list(ProductComanda.objects.values('product').annotate(
    quantidade=Count('product'),
    nome=F('product__name') ).order_by('-quantidade'))

    products = Product.objects.filter(active=True).exclude(
        category__name__in=['Insumos', 
        'Adicional', 
        'Bomboniere',
        'Lojinha',
        'Utensilios',
        'Litros',
        'Ingressos',
        'Cigarros',
        'Outros']
        )




    products_ordenados = []
    for produto in produtos_mais_vendidos:
        for p in products:
            if p.name == produto['nome']:
                products_ordenados.append(p)




    product_list = []
    for product in products_ordenados:
        product_data = {
            "id": product.id,
            "name": product.name,
            "description": product.description or "",
            "price": float(product.price),
            "category": product.category.name if product.category else "",
            "image": str(product.image) if product.image else f"https://placehold.co/400x250/efc7b8/49291c?text={product.name.replace(' ', '+')}"
        }
        product_list.append(product_data)

    # Retorna como JSON em texto simples
    return HttpResponse(
        json.dumps(product_list, indent=4, ensure_ascii=False),
         content_type="application/json; charset=utf-8"
    )

