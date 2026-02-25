from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count, F
from django.contrib.auth.models import User




from comandas.models import Comanda, ProductComanda, StockMovementType, StockMovement
from mesas.models import Mesa
from products.models import Product
from payments.models import Payments
from typePay.models import TypePay
from gestaoRaul.decorators import group_required

def listProductBalcao(request, comanda_id, search_product):
    comanda_id = request.GET.get("id-comanda-balcao")
    if search_product == '*':
        products_ordenados = ProductComanda.maisVendidos()         

        return render(request, "htmx_components/htmx_list_products_balcao.html", {"products": products_ordenados,'comanda_id':comanda_id})
    else:
        product = search_product
        products = Product.objects.filter(name__icontains=product, active=True)
        return render(request, "htmx_components/htmx_list_products_balcao.html", {"products": products[:15],'comanda_id':comanda_id})


@group_required(groupName='Garçom')
def addProductBalcao(request, product_id, comanda_id, qtd):
    for i in range(qtd):
        product_comanda = ProductComanda(comanda_id=comanda_id, product_id=product_id)
        product_comanda.save()
        product = Product.objects.get(id=product_id)
        comanda = Comanda.objects.get(id=comanda_id)
        user = User.objects.get(id=request.user.id)
        typeMovement = StockMovementType.objects.get(name="Venda - Balcao")

        StockMovement.subTransactionStock(
            product=product,
            movement_type=typeMovement,
            comanda=comanda,
            user=user,
            qtd=1,
            obs= "Vendido no balcão"
        )

    consumo = ProductComanda.objects.filter(comanda=comanda_id)
    total = 0
    for produto in consumo:
        total += produto.product.price
    return render(request, "htmx_components/htmx_list_products_in_balcao.html",{'consumo': consumo, 'total': total})

@group_required(groupName='Garçom')
@csrf_exempt
def addProductBalcaoTeclado(request, product_id, comanda_id, qtd):
    for i in range(qtd):
        product_comanda = ProductComanda(comanda_id=comanda_id, product_id=product_id)
        product_comanda.save()
        product = Product.objects.get(id=product_id)
        comanda = Comanda.objects.get(id=comanda_id)
        user = User.objects.get(id=request.user.id)
        typeMovement = StockMovementType.objects.get(name="Venda - Balcao")

        StockMovement.subTransactionStock(
            product=product,
            movement_type=typeMovement,
            comanda=comanda,
            user=user,
            qtd=1,
            obs= "Vendido no balcão"
        )

    consumo = ProductComanda.objects.filter(comanda=comanda_id)
    total = 0
    for produto in consumo:
        total += produto.product.price
    return render(request, "htmx_components/htmx_list_products_in_balcao.html",{'consumo': consumo, 'total': total})

@group_required(groupName='Garçom')
def removeProductBalcao(request, productComanda_id):
    product_comanda = ProductComanda.objects.get(id=productComanda_id)
    comanda = product_comanda.comanda
    product = product_comanda.product
    user = User.objects.get(id=request.user.id)
    typeMovement = StockMovementType.objects.get(name="Estorno")

    consumo = ProductComanda.objects.filter(comanda=product_comanda.comanda)
    StockMovement.sumTransactionStock(
                    product=product,
                    movement_type=typeMovement,
                    comanda=comanda,
                    user=user,
                    qtd=1,
                    obs= "Excluido do balcão"
                )
    
    
    product_comanda.delete()

    total = 0
    for produto in consumo:
        total += produto.product.price
    return render(request, "htmx_components/htmx_list_products_in_balcao.html",{'consumo': consumo, 'total': total})

@group_required(groupName='Garçom')
def paymentBalcao(request, comanda_id):
    typePayment = TypePay.objects.get(id=1)
    consumo = ProductComanda.objects.filter(comanda=comanda_id)
    user = User.objects.get(id=request.user.id)
    try:
        vendasBalcao = Comanda.objects.get(name='VENDAS BALCAO')
    except:
        mesa = Mesa.objects.get(id=1)
        vendasBalcao = Comanda(name='VENDAS BALCAO', mesa=mesa, user=request.user, status='CLOSED')
        vendasBalcao.save()
    comanda = Comanda.objects.get(name=f'{user.id} - BALCÃO - {user.first_name}')
    total = 0
    for produto in consumo:
        total += produto.product.price
        produto.comanda = vendasBalcao
        produto.save()
    pagamento = Payments(value=total, comanda=comanda, type_pay=typePayment,description=f'{user.id} - BALCÃO - {user.first_name}')
    pagamento.save()
    return redirect('viewBalcao')

