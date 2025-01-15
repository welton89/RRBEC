from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from gestaoRaul.decorators import group_required
from clients.models import Client



@group_required(groupName='Gerente')
def clients(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', {'clients': clients})


@group_required(groupName='Gerente')
def createClient(request):
    name = request.POST.get('name')
    contact = request.POST.get('contact')
    active = True if request.POST.get('active') else False
    # debt = request.POST.get('debt')
    client = Client(name=name, contact=contact,debt=0, active=active)
    client.save()
    return redirect('/clients')

def payDebt(request):
    # id = request.POST.get('id-client')
    # client_id = int(id)
    # client = Client.objects.get(id=client_id)
    # client.debt = client.debt - 1
    # client.save()
    return redirect('/clients')