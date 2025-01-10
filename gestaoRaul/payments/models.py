from django.db import models
from typePay.models import TypePay
from comandas.models import Comanda
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