from django.db import models

from products.models import Product
from comandas.models import Comanda, ProductComanda


class Order(models.Model):
    productComanda = models.ForeignKey(ProductComanda, on_delete=models.SET_NULL, null=True)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    id_comanda = models.ForeignKey(Comanda, on_delete=models.CASCADE)
    obs = models.TextField(blank=True, null=True)
    queue = models.DateTimeField(auto_now_add=True)
    preparing = models.DateTimeField(null=True, blank=True)
    finished = models.DateTimeField(null=True, blank=True)
    delivered = models.DateTimeField(null=True, blank=True)
    canceled = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Pedido {self.id} - Produto: {self.id_product} - Comanda: {self.id_comanda.name}"