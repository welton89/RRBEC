from django.contrib import admin

from comandas.models import Comanda, ProductComanda

admin.site.register(Comanda)
admin.site.register(ProductComanda)

