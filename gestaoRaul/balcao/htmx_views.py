from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count, F



from comandas.models import Comanda, ProductComanda
from mesas.models import Mesa
from products.models import Product
from payments.models import Payments
from typePay.models import TypePay

def listProductBalcao(request, comanda_id, search_product):
    if search_product == '*':
        produtos_mais_vendidos = list(ProductComanda.objects.values('product').annotate(
        quantidade=Count('product'),
        nome=F('product__name') ).order_by('-quantidade'))
        products = Product.objects.all()
        products_ordenados = []

        for produto in produtos_mais_vendidos:
            for p in products:
                if p.active == True and p.name == produto['nome']:
                        products_ordenados.append(p)
          

        return render(request, "htmx_components/htmx_list_products_balcao.html", {"products": products_ordenados,'comanda_id':comanda_id})
    else:
        product = search_product
        products = Product.objects.filter(name__icontains=product, active=True)
        return render(request, "htmx_components/htmx_list_products_balcao.html", {"products": products,'comanda_id':comanda_id})



def addProductBalcao(request, product_id, comanda_id, qtd):
    for i in range(qtd):
        product_comanda = ProductComanda(comanda_id=comanda_id, product_id=product_id)
        product_comanda.save()
    consumo = ProductComanda.objects.filter(comanda=comanda_id)
    total = 0
    for produto in consumo:
        total += produto.product.price
    return render(request, "htmx_components/htmx_list_products_in_balcao.html",{'consumo': consumo, 'total': total})

@csrf_exempt
def addProductBalcaoTeclado(request, product_id, comanda_id, qtd):
    for i in range(qtd):
        product_comanda = ProductComanda(comanda_id=comanda_id, product_id=product_id)
        product_comanda.save()
    consumo = ProductComanda.objects.filter(comanda=comanda_id)
    total = 0
    for produto in consumo:
        total += produto.product.price
    return render(request, "htmx_components/htmx_list_products_in_balcao.html",{'consumo': consumo, 'total': total})


def removeProductBalcao(request, productComanda_id):
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
    try:
        vendasBalcao = Comanda.objects.get(name='VENDAS BALCAO')
    except:
        mesa = Mesa.objects.get(id=1)
        vendasBalcao = Comanda(name='VENDAS BALCAO', mesa=mesa, user=request.user, status='CLOSED')
        vendasBalcao.save()
    comanda = Comanda.objects.get(name='VENDA BALCÃO')
    total = 0
    for produto in consumo:
        total += produto.product.price
        produto.comanda = vendasBalcao
        produto.save()
    pagamento = Payments(value=total, comanda=comanda, type_pay=typePayment,description='VENDA BALCÃO')
    pagamento.save()
    return redirect('viewBalcao')



#"GET /balcao/addProductBalcaoTeclado83/1/1/ HTTP/1.1" 200 747
#"GET /balcao/addProductBalcaoTeclado83/13/1/ HTTP/1.1" 500 133103