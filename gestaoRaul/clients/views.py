from decimal import Decimal
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from comandas.models import Comanda, ProductComanda
from gestaoRaul.decorators import group_required
from clients.models import Client
from payments.models import Payments



@group_required(groupName='Gerente')
def clients(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', {'clients': clients})

def viewClient(request,clientId):
    # config = {
    #     'taxa': False
    # }
    client = Client.objects.get(id=int(clientId))
    comandas = Comanda.objects.filter(client = client).filter(status = 'FIADO')
    total = Decimal(0)
    # for comanda in comandas:
    #     totalConsumo = 0
    #     totalParcial = 0
    #     consumo = ProductComanda.objects.filter(comanda=comanda)
    #     parcial = Payments.objects.filter(comanda=comanda)
    #     for p in parcial:
    #         totalParcial += p.value
    #     for produto in consumo:
    #         totalConsumo += produto.product.price
    #     total+= (totalConsumo - totalParcial)
    # total = total + round(total * Decimal(0.1), 2) if config['taxa'] else total
    return render(request, 'viewclient.html', {'client': client, 'comandas': comandas})


@group_required(groupName='Gerente')
def createClient(request):
    name = request.POST.get('name')
    contact = request.POST.get('contact')
    active = True if request.POST.get('active') else False
    # debt = request.POST.get('debt')
    client = Client(name=name, contact=contact,debt=0, active=active)
    client.save()
    return redirect('/clients')

@group_required(groupName='Gerente')
def editClient(request):
    client_id = int(request.POST.get('clientId'))
    client = Client.objects.get(id=client_id)
    client.name = request.POST.get('name')
    client.contact = request.POST.get('contact')
    client.active = True if request.POST.get('active') else False
    # client = Client(name=name, contact=contact,debt=0, active=active)
    client.save()
    return redirect('/clients')

def payDebt(request):
    # id = request.POST.get('id-client')
    # client_id = int(id)
    # client = Client.objects.get(id=client_id)
    # client.debt = client.debt - 1
    # client.save()
    return redirect('/clients')