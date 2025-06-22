from django.db import models
from decimal import Decimal

from typePay.models import TypePay
from comandas.models import Comanda, ProductComanda
from clients.models import Client


class Payments(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    type_pay = models.ForeignKey(TypePay, on_delete=models.PROTECT)
    comanda = models.ForeignKey(Comanda, on_delete=models.PROTECT)
    client = models.ForeignKey(Client, null=True , on_delete=models.PROTECT)
    description = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.comanda.name


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