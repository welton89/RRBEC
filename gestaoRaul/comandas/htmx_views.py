from django.http import JsonResponse
from django.shortcuts import render, redirect

from comandas.models import Comanda, ProductComanda
from orders.models import Order
from products.models import Product
from payments.models import Payments
from typePay.models import TypePay
from gestaoRaul.decorators import group_required


def listProduct(request, comanda_id):
    product = request.GET.get("search-product")
    allProducts = Product.objects.filter(name__icontains=product)
    products = []
    for p in allProducts:
        if p.active == True:
            products.append(p)
    return render(request, "htmx_components/htmx_list_products.html", {"products": products,'comanda_id':comanda_id})

@group_required(groupName='Garçom')
def addProduct(request, product_id, comanda_id):
    obs = request.GET.get("obs")
    product_comanda = ProductComanda(comanda_id=comanda_id, product_id=product_id)
    product_comanda.save()
    product = Product.objects.get(id=product_id)
    comanda = Comanda.objects.get(id=comanda_id)
    print(product.cuisine)

    if product.cuisine == True:
        order = Order(id_comanda=comanda, id_product=product, productComanda=product_comanda, obs='')
        order.save()
    consumo = ProductComanda.objects.filter(comanda=comanda_id)
    total = 0
    for produto in consumo:
        total += produto.product.price
    return render(request, "htmx_components/htmx_list_products_in_comanda.html",{'consumo': consumo, 'total': total, 'comanda':comanda})

@group_required(groupName='Garçom')
def editOrders(request, productComanda_id, obs):
    order = Order.objects.get(productComanda=productComanda_id)
    print(obs)
    order.obs = obs
    order.save()
    return JsonResponse({'status': 'ok'})


@group_required(groupName='Garçom')
def removeProductComanda(request, productComanda_id):
    product_comanda = ProductComanda.objects.get(id=productComanda_id)
    comanda = Comanda.objects.get(id= product_comanda.comanda.id)
    consumo = ProductComanda.objects.filter(comanda=comanda)

    product_comanda.delete()
    total = 0
    for produto in consumo:
        total += produto.product.price
    return render(request, "htmx_components/htmx_list_products_in_comanda.html",{'consumo': consumo, 'total': total, 'comanda':comanda})

@group_required(groupName='Garçom')
def closeComanda(request, comanda_id):
    comanda = Comanda.objects.get(id=comanda_id)
    comanda.status = "PAYING"
    comanda.save()


@group_required(groupName='Gerente')
def reopenComanda(request, comanda_id):
    comanda = Comanda.objects.get(id=comanda_id)
    if comanda.status == 'CLOSED':
        pass
    else:
        comanda.status = "OPEN"
        comanda.save()

@group_required(groupName='Gerente')
def paymentComanda(request, comanda_id):
    typePayment = TypePay.objects.get(id=1)
    consumo = ProductComanda.objects.filter(comanda=comanda_id)
    comanda = Comanda.objects.get(id=comanda_id)
    total = 0
    for produto in consumo:
        total += produto.product.price
    pagamento = Payments(value=total, comanda=comanda, type_pay=typePayment,description='tipo de pagamento mokado')
    pagamento.save()
    comanda.status = 'CLOSED'
    comanda.save()
    return redirect('/comandas')
