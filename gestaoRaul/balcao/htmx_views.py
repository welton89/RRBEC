from django.shortcuts import render, redirect

from comandas.models import Comanda, ProductComanda
from products.models import Product
from payments.models import Payments
from typePay.models import TypePay


def listProductBalcao(request, comanda_id):
    product = request.GET.get("search-product")
    products = Product.objects.filter(name__icontains=product)
    print(products)
    return render(request, "htmx_components/htmx_list_products_balcao.html", {"products": products,})

def addProductBalcao(request, product_id, comanda_id, qtd):
    for i in range(qtd):
        product_comanda = ProductComanda(comanda_id=comanda_id, product_id=product_id)
        product_comanda.save()
    consumo = ProductComanda.objects.filter(comanda=comanda_id)
    total = 0
    for produto in consumo:
        total += produto.product.price
    return render(request, "htmx_components/htmx_list_products_in_balcao.html",{'consumo': consumo, 'total': total})


def addProductBalcaoTeclado(request, product_id, comanda_id, qtd):
    print('entrouuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu', product_id, comanda_id)
    for i in range(qtd):
        product_comanda = ProductComanda(comanda_id=comanda_id, product_id=product_id)
        product_comanda.save()
    consumo = ProductComanda.objects.filter(comanda=comanda_id)
    total = 0
    for produto in consumo:
        total += produto.product.price
    return render(request, "htmx_components/htmx_list_products_in_balcao.html",{'consumo': consumo, 'total': total})


def removeProductBalcao(request, productComanda_id):
    print(request.COOKIES['qtd'])
    product_comanda = ProductComanda.objects.get(id=productComanda_id)
    consumo = ProductComanda.objects.filter(comanda=product_comanda.comanda)
    product_comanda.delete()
    total = 0
    for produto in consumo:
        total += produto.product.price
    return render(request, "htmx_components/htmx_list_products_in_balcao.html",{'consumo': consumo, 'total': total})


def paymentBalcao(request, comanda_id):
    typePayment = TypePay.objects.get(id=1)
    consumo = ProductComanda.objects.filter(comanda=comanda_id)
    vendasBalcao = Comanda.objects.get(name='VENDAS BALCAO')
    comanda = Comanda.objects.get(name='VENDA BALCÃO')
    total = 0
    for produto in consumo:
        total += produto.product.price
        produto.comanda = vendasBalcao
        produto.save()
    pagamento = Payments(value=total, comanda=comanda, type_pay=typePayment,description='VENDA BALCÃO')
    pagamento.save()
    # comanda.save()
    return redirect('viewBalcao')

