from decimal import Decimal
from django.urls import reverse
from django.utils import timezone

from django.http import JsonResponse, HttpResponseRedirect

from django.shortcuts import render, redirect
from django.db.models import Count, F

from comandas.models import Comanda, ProductComanda
from clients.models import Client
from payments.models import Payments, somar
from orders.models import Order
from products.models import Product
from mesas.models import Mesa
from gestaoRaul.decorators import group_required


@group_required(groupName='Garçom')
def comandas(request):
    comandas = Comanda.objects.filter(status__in=["OPEN", "PAYING"])
    mesas = Mesa.objects.all()
    return render(request, 'comandas.html', {'comandas': comandas, 'mesas': mesas})


@group_required(groupName='Garçom')
def viewComanda(request):
    config = {
        'taxa': False
        }
    id = request.GET.get('parametro')
    comanda_id = int(id)
    comanda = Comanda.objects.get(id=comanda_id)
    consumo = ProductComanda.objects.filter(comanda=comanda_id)
    # consumo[0].product.
    parcial = Payments.objects.filter(comanda=comanda_id)
    mesas = Mesa.objects.all()
    clients = Client.objects.filter(active=True)

    produtos_mais_vendidos = list(ProductComanda.objects.values('product').annotate(
    quantidade=Count('product'),
    nome=F('product__name') ).order_by('-quantidade'))

    products = Product.objects.all()
    products_ordenados = []
    for produto in produtos_mais_vendidos:
        for p in products:
            if p.name == produto['nome'] and p.active == True:
                products_ordenados.append(p)
    valores = somar(consumo,comanda)
    
    return render(request, 'viewcomanda.html', {'config':config, 'valores':valores,'parcials':parcial,'clients':clients,'comanda': comanda, 'consumo': consumo, 'products': products_ordenados,'mesas':mesas})


@group_required(groupName='Garçom')
def createComanda(request):
    name = request.POST.get('name-comanda')
    if name == '' or name == None or request.POST.get('select-mesa') == '' or request.POST.get('select-mesa') == None:
        return HttpResponseRedirect(reverse('comandas'), status=400)
    mesa_id = int(request.POST.get('select-mesa'))
    mesa = Mesa.objects.get(id=mesa_id)
    comanda = Comanda(name=name, mesa=mesa, user=request.user)
    comanda.save()
    return redirect(reverse('viewcomanda') + f'?parametro={comanda.id}')


@group_required(groupName='Garçom')
def editComanda(request):
    name = request.POST.get('nameComanda')
    comanda = Comanda.objects.get(id=int(request.POST.get('h-comandaId')))
    mesa = Mesa.objects.get(id=int(request.POST.get('select-mesa')))
    comanda.mesa = mesa
    comanda.name = name
    comanda.save()
    return redirect('comandas')

@group_required(groupName='Gerente')
def addContaCliente(request):
   
    comandaId = int(request.POST.get('idComanda'))
    clientId = int(request.POST.get('select-client'))
    comanda = Comanda.objects.get(id=comandaId)
    client = Client.objects.get(id=clientId)
    comanda.client = client
    comanda.dt_close = timezone.now()
    comanda.status = 'FIADO'
    client.save()
    comanda.save()
    return redirect('comandas')

def notificacao(request):
    fifteen_hours_ago = timezone.now() - timezone.timedelta(hours=12)
    ordersPronto = Order.objects.filter(queue__gte=fifteen_hours_ago, finished__isnull=False)

    grupoGarcom = request.user.groups.filter(name='Garçom').exists()
    grupoGerente = request.user.groups.filter(name='Gerente').exists()

    if grupoGarcom == True and grupoGerente == False:
        if 'pronto' in request.COOKIES:
            cookiesPronto = int(request.COOKIES['pronto'])
            if len(ordersPronto) > cookiesPronto:
                return JsonResponse({
                        'notificacao': 'true',
                        'pronto':len(ordersPronto),
                        'titulo': ordersPronto[len(ordersPronto)-1].id_comanda.name,
                        'corpo': ordersPronto[len(ordersPronto)-1].id_product.name,
                    })
            else:
                return JsonResponse({
                        'notificacao': 'false',
                        'pronto': len(ordersPronto),
                    })
        else:
            return JsonResponse({
            'notificacao': 'true',
            'pronto':len(ordersPronto),
            'titulo': ordersPronto[len(ordersPronto)-1].id_comanda.name,
            'corpo': ordersPronto[len(ordersPronto)-1].id_product.name,
             })


    else:
        return JsonResponse({
            'notificacao': 'false',
            'pronto':len(ordersPronto),
             })



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
    # asyncio.run(enviar_mensagem(msg))
    return JsonResponse({'status': 'ok', 'obs':order.obs})


@group_required(groupName='Garçom')
def closeComanda(request, comanda_id):
    comanda = Comanda.objects.get(id=comanda_id)
    comanda.status = "PAYING"
    comanda.save()
    return JsonResponse({'status': 'ok', 'obs':'order.obs'})

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
                                <form method="path" action="/pedidos/preparing/{order.id}/">
                                <button class="btn-primary" type="submit">Preparar</button>
                                </form>
                                </div>
                                """, 
              'local':'cozinha',
                'tipo':'add',
                  'id':order.id,
                  'speak': f'Novo pedido!  {product.name}, para {comanda.name}.'
                  }) 
        try:
        # Chama a função async dentro da view normal
            async_to_sync(enviar_mensagem)(mensagem)

            # return JsonResponse({"status": "Mensagem enviada com sucesso"})

        except Exception as e:
            print("Erro add product websocket: ",e)
            # return JsonResponse({"status": "Erro", "erro": str(e)}, status=500)
        # asyncio.run(enviar_mensagem(msg))
    consumo = ProductComanda.objects.filter(comanda=comanda_id)
    valores = somar(consumo,comanda)
    
    return render(request, "htmx_components/comandas/htmx_list_products_in_comanda.html",{'config':config, 'valores':valores,'parcials':parcial,'consumo': consumo,'comanda':comanda})



def listProduct(request, comanda_id, product):
    allProducts = Product.objects.filter(name__icontains=product)
    products = []
    for p in allProducts:
        if p.active == True:
            products.append(p)
    return render(request, "htmx_components/comandas/htmx_list_products.html", {"products": products,'comanda_id':comanda_id})