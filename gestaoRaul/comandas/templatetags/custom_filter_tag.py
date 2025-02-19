from decimal import Decimal
from django import template

from comandas.models import Comanda, ProductComanda
from payments.models import Payments

register = template.Library()

@register.filter(name='total')
def filter_total(value):
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
    total = (total + taxa) - totalParcial
    return f'R$ {total}'


@register.filter(name='groupUser')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()