from django import template

from comandas.models import Comanda, ProductComanda

register = template.Library()

@register.filter(name='total')
def filter_total(value):
    id = value
    comanda_id = int(id)
    consumo = ProductComanda.objects.filter(comanda=comanda_id)
    total = 0
    for produto in consumo:
        total += produto.product.price
    return f'R$ {total}'