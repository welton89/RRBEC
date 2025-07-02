from decimal import Decimal
from django import template

from orders.models import  Order
from comandas.models import Comanda, ProductComanda
from clients.models import Client
from payments.models import Payments

register = template.Library()

@register.filter(name='total')
def filter_total(value):
    config = {
        'taxa': False
    }    
    id = value
    comanda_id = int(id)
    totalParcial = Decimal(0)
    comanda = Comanda.objects.get(id=comanda_id)
    consumo = ProductComanda.objects.filter(comanda=comanda_id)
    parcial = Payments.objects.filter(comanda=comanda)
    for p in parcial:
        totalParcial += p.value

    total = Decimal(0)
    for produto in consumo:
        total += produto.product.price
    taxa = round(total * Decimal(0.1), 2)
    total = (total + taxa) - totalParcial if config['taxa'] else total - totalParcial
    return f'R$ {total}'

@register.filter(name='totalFiado')
def viewClient(clientId):
    config = {
        'taxa': False
    }
    client = Client.objects.get(id=int(clientId))
    comandas = Comanda.objects.filter(client = client).filter(status = 'FIADO')
    total = Decimal(0)
    for comanda in comandas:
        totalConsumo = 0
        totalParcial = 0
        consumo = ProductComanda.objects.filter(comanda=comanda)
        parcial = Payments.objects.filter(comanda=comanda)
        for p in parcial:
            totalParcial += p.value
        for produto in consumo:
            totalConsumo += produto.product.price
        total+= (totalConsumo - totalParcial)
    total = total + round(total * Decimal(0.1), 2) if config['taxa'] else total
    return total



@register.filter(name='groupUser')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()


@register.filter(name='obsOrder')
def obsOrder(id):
    try:
        productComanda_obj = ProductComanda.objects.get(pk=id)    
        order = Order.objects.get(productComanda=productComanda_obj)
        return order
    except:
        return ''
    
   