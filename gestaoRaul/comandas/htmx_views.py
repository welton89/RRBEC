from decimal import Decimal
from django.http import JsonResponse
from django.shortcuts import render, redirect

from comandas.models import Comanda, ProductComanda
from orders.models import Order
from products.models import Product
from payments.models import Payments
from typePay.models import TypePay
from gestaoRaul.decorators import group_required


def somar(consumo:ProductComanda, comanda:Comanda):
    parcial = Payments.objects.filter(comanda=comanda)
    totalParcial = Decimal(0)
    total:Decimal = Decimal(0)
    for p in parcial:
        totalParcial += p.value
    for produto in consumo:
        total += Decimal(produto.product.price)
    valores = {
        'total':total,
        'parcial':totalParcial,
        'taxaTotal': round(total * Decimal(0.1), 2)
    }
    return valores

def listProduct(request, comanda_id):
    product = request.GET.get("search-product")
    allProducts = Product.objects.filter(name__icontains=product)
    products = []
    for p in allProducts:
        if p.active == True:
            products.append(p)
    return render(request, "htmx_components/comandas/htmx_list_products.html", {"products": products,'comanda_id':comanda_id})

@group_required(groupName='Garçom')
def addProduct(request, product_id, comanda_id):
    obs = request.GET.get("obs")
    product_comanda = ProductComanda(comanda_id=comanda_id, product_id=product_id)
    product_comanda.save()
    product = Product.objects.get(id=product_id)
    comanda = Comanda.objects.get(id=comanda_id)
    parcial = Payments.objects.filter(comanda=comanda)
    if product.cuisine == True:
        order = Order(id_comanda=comanda, id_product=product, productComanda=product_comanda, obs='')
        order.save()
    consumo = ProductComanda.objects.filter(comanda=comanda_id)
    valores = somar(consumo,comanda)
    total = valores['total'] - valores['parcial']
    return render(request, "htmx_components/comandas/htmx_list_products_in_comanda.html",{'parcials':parcial,'consumo': consumo, 'total': total, 'comanda':comanda})

@group_required(groupName='Garçom')
def editOrders(request, productComanda_id, obs):
    order = Order.objects.get(productComanda=productComanda_id)
    order.obs = obs
    order.save()
    return JsonResponse({'status': 'ok'})


@group_required(groupName='Garçom')
def removeProductComanda(request, productComanda_id):
    product_comanda = ProductComanda.objects.get(id=productComanda_id)
    comanda = Comanda.objects.get(id= product_comanda.comanda.id)
    parcial = Payments.objects.filter(comanda=comanda)
    consumo = ProductComanda.objects.filter(comanda=comanda)
    product_comanda.delete()
    valores = somar(consumo,comanda)
    total = valores['total'] - valores['parcial']
    return render(request, "htmx_components/comandas/htmx_list_products_in_comanda.html",{'parcials':parcial,'consumo': consumo, 'total': total, 'comanda':comanda})

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
    valores = somar(consumo,comanda)
    total = valores['total'] - valores['parcial']
    pagamento = Payments(value=total, comanda=comanda, type_pay=typePayment,description='tipo de pagamento mokado')
    pagamento.save()
    comanda.status = 'CLOSED'
    comanda.save()
    return redirect('/comandas')

@group_required(groupName='Gerente')
def paymentParcial(request, comanda_id):
    typePayment = TypePay.objects.get(id=1)
    comanda = Comanda.objects.get(id=comanda_id)
    value = Decimal(request.POST.get('value-parcial'))
    print(value)
    description = request.POST.get('name-parcial')
    pagamento = Payments(value=value, comanda=comanda, type_pay=typePayment,description=description)
    pagamento.save()
    return redirect('/comandas')
