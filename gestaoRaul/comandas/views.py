from decimal import Decimal
from django.utils import timezone

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.db.models import Count, F

from comandas.models import Comanda, ProductComanda
from clients.models import Client
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
    id = request.GET.get('parametro')
    comanda_id = int(id)
    comanda = Comanda.objects.get(id=comanda_id)
    consumo = ProductComanda.objects.filter(comanda=comanda_id)
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
    total = 0
    for produto in consumo:
        total += produto.product.price
  
    return render(request, 'viewcomanda.html', {'clients':clients,'comanda': comanda, 'consumo': consumo, 'total': total, 'products': products_ordenados,'mesas':mesas})


@group_required(groupName='Garçom')
def createComanda(request):
    name = request.POST.get('name-comanda')
    mesa_id = int(request.POST.get('select-mesa'))
    mesa = Mesa.objects.get(id=mesa_id)
    comanda = Comanda(name=name, mesa=mesa, user=request.user)
    comanda.save()
    return redirect('comandas')

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
    valor = float(request.POST.get('valor-conta').replace(',','.'))
    comanda = Comanda.objects.get(id=comandaId)
    client = Client.objects.get(id=clientId)
    client.debt = client.debt + Decimal(valor)
    comanda.client = client
    comanda.status = 'CLOSED'
    client.save()
    comanda.save()
    return redirect('comandas')

def notificacao(request):
    fifteen_hours_ago = timezone.now() - timezone.timedelta(hours=15)
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
