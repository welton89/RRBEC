# from django.db import models

# from clients.models import Client
# from products.models import Product
# from mesas.models import Mesa
# from typePay.models import TypePay

# class Comanda(models.Model):
#     id = models.AutoField(primary_key=True)
#     mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
#     type_pay = models.ForeignKey(TypePay, on_delete=models.SET_NULL, null=True)
#     dt_open = models.DateTimeField(auto_now_add=True)
#     dt_close = models.DateTimeField(null=True, blank=True)
#     client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
#     name = models.CharField(max_length=255)
#     status = models.CharField(max_length=255, default="OPEN")
#     def __str__(self) -> str:
#         return self.name

# class ProductComanda(models.Model):
#     id = models.AutoField(primary_key=True)
#     comanda = models.ForeignKey(Comanda, on_delete=models.CASCADE)
#     data_time = models.DateTimeField(auto_now_add=True)
#     product = models.ForeignKey(Product, on_delete=models.PROTECT)
#     applicant = models.CharField(max_length=255, null=True, blank=True)
#     def __str__(self) -> str:
#         return self.comanda.name + " - " + self.product.name