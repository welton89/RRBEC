from django.contrib import admin

from categories.models import Categories
from clients.models import Client
from comandas.models import Comanda
from typePay.models import TypePay
from products.models import Product
from mesas.models import Mesa


admin.site.register(Mesa)
admin.site.register(Product)
admin.site.register(Categories)
admin.site.register(Client)
admin.site.register(Comanda)
admin.site.register(TypePay)

# Register your models here.
