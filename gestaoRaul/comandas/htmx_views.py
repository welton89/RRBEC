from datetime import date
from decimal import Decimal
from django.http import JsonResponse
from django.shortcuts import render, redirect

from comandas.models import Comanda, ProductComanda
from orders.models import Order
from products.models import Product
from payments.models import Payments
from typePay.models import TypePay
from gestaoRaul.decorators import group_required

import asyncio
import websockets

async def enviar_mensagem(msg):
    uri = "ws://192.168.1.150:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send(msg)
        print(f"> Enviado: {msg}")

        resposta = await websocket.recv()
        print(f"< Recebido: {resposta}")




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
        'taxa': round(total * Decimal(0.1), 2),
        'totalSemTaxa':total - totalParcial,
        'totalComTaxa': round((total - totalParcial)+(total * Decimal(0.1)),2)
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
    config = {
        'taxa': False
        }
    obs = request.GET.get("obs")
    product_comanda = ProductComanda(comanda_id=comanda_id, product_id=product_id)
    product_comanda.save()
    product = Product.objects.get(id=product_id)
    comanda = Comanda.objects.get(id=comanda_id)
    parcial = Payments.objects.filter(comanda=comanda)
    if product.cuisine == True:
        order = Order(id_comanda=comanda, id_product=product, productComanda=product_comanda, obs='')
        order.save()
        msg = JsonResponse({
            'type': 'broadcast',
              'message': f"""
                                <div class="m-card" id="m-card-{order.id}">
                                <h4>{product.name}</h4>
                                <h4 id="obs-{order.id}"> {order.obs}</h4>
                                <h4>{comanda.name} - {comanda.mesa.name}</h4>
                                <h4> {order.queue.strftime("%d/%m/%Y - %H:%M")}</h4>
                                <h4> Atendente: {comanda.user.first_name}</h4>
                                <button class="btn-primary" onclick="delayTab('Fila')"
                                hx-get="/pedidos/preparing/{order.id}/" hx-trigger="click" hx-target="#etapas"
                                >Preparar</button></div>
                                """, 
              'local':'cozinha',
                'tipo':'add',
                  'id':order.id,
                  'speak': f'Novo pedido!  {product.name}, para {comanda.name}.'
                  }) 
        asyncio.run(enviar_mensagem(msg))
    consumo = ProductComanda.objects.filter(comanda=comanda_id)
    valores = somar(consumo,comanda)
    
    return render(request, "htmx_components/comandas/htmx_list_products_in_comanda.html",{'config':config, 'valores':valores,'parcials':parcial,'consumo': consumo,'comanda':comanda})

@group_required(groupName='Garçom')
def editOrders(request, productComanda_id, obs):
    order = Order.objects.get(productComanda=productComanda_id)
    order.obs = obs
    order.save()
    msg = JsonResponse({
            'type': 'broadcast',
              'message': obs, 
              'local':'cozinha',
                'tipo':'edit',
                  'id':order.id,
                  'speak': f'Pedido alterado!  {order.id_product.name}, é {obs}.'
                  }) 
    asyncio.run(enviar_mensagem(msg))
    return JsonResponse({'status': 'ok'})


@group_required(groupName='Garçom')
def removeProductComanda(request, productComanda_id):
    config = {
        'taxa': False
        }
    product_comanda = ProductComanda.objects.get(id=productComanda_id)
    comanda = Comanda.objects.get(id= product_comanda.comanda.id)
    parcial = Payments.objects.filter(comanda=comanda)
    consumo = ProductComanda.objects.filter(comanda=comanda)
    valores = somar(consumo,comanda)
    if product_comanda.product.cuisine == True:
        order = Order.objects.get(productComanda=product_comanda)
        product_comanda.delete()
        msg = JsonResponse({
            'type': 'broadcast',
              'message': 'Atenção! Pedido cancelado', 
              'local':'cozinha',
                'tipo':'delete',
                  'id':order.id,
                  'speak': f'Pedido cancelado!  {order.id_product.name}.'
                  }) 
        asyncio.run(enviar_mensagem(msg))
        # order.delete()
    else:
        product_comanda.delete()

    return render(request, "htmx_components/comandas/htmx_list_products_in_comanda.html",{'config':config, 'valores': valores,'parcials':parcial,'consumo': consumo, 'comanda':comanda})

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
    taxa = request.POST.get('taxa',False)
    typePayment = TypePay.objects.get(id=1)
    consumo = ProductComanda.objects.filter(comanda=comanda_id)
    comanda = Comanda.objects.get(id=comanda_id)
    valores = somar(consumo,comanda)
    if taxa == 'True':
        pagamento = Payments(value=valores['totalComTaxa'], comanda=comanda, type_pay=typePayment,description='tipo de pagamento mokado')
        pagamento.save()
    else:
        pagamento = Payments(value=valores['totalSemTaxa'], comanda=comanda, type_pay=typePayment,description='tipo de pagamento mokado')
        pagamento.save()

    comanda.status = 'CLOSED'
    comanda.save()
    return redirect('/comandas')

@group_required(groupName='Gerente')
def paymentParcial(request, comanda_id):
    typePayment = TypePay.objects.get(id=1)
    comanda = Comanda.objects.get(id=comanda_id)
    value = Decimal(request.POST.get('value-parcial'))
    description = request.POST.get('name-parcial')
    pagamento = Payments(value=value, comanda=comanda, type_pay=typePayment,description=description)
    pagamento.save()
    return redirect('/comandas')
