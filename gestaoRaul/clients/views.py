from decimal import Decimal
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json

from comandas.models import Comanda, ProductComanda
from gestaoRaul.decorators import group_required
from clients.models import Client
from payments.models import Payments, somar
from typePay.models import TypePay

# Create your views here.




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


@csrf_exempt
@require_POST
def payDebt(request):
    try:
        # Verifica se é uma requisição AJAX
        if not request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'error': 'Requisição inválida'}, status=400)
        
        # Obter os IDs do corpo da requisição (não mais da URL)
        try:
            data = json.loads(request.body)
            comanda_ids = data.get('ids', [])
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=400)
        
        for comanda_id in comanda_ids:
            try:
                comanda = Comanda.objects.get(id=comanda_id)
                comanda.status = 'CLOSED'
                comanda.save()

                typePayment = TypePay.objects.get(id=1)
                consumo = ProductComanda.objects.filter(comanda=comanda_id)
                value = somar(consumo,comanda)
                print(value["totalSemTaxa"])
                description = 'PAGAMENTO DE FIADO'
                pagamento = Payments(value=value["totalSemTaxa"], comanda=comanda, type_pay=typePayment,description=description,client=comanda.client)
                pagamento.save()
            except Comanda.DoesNotExist:
                return JsonResponse({'error': f'Comanda com ID {comanda_id} não encontrada'}, status=404)
        
        return redirect(f'/clients/viewClient/{comanda.client.id}')
        
        # return JsonResponse({
        #     'success': True,
        #     'message': f'{len(comanda_ids)} comandas processadas',
        #     'ids': comanda_ids
        # }, status=200)
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)