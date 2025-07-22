from django.contrib import admin

from comandas.models import Comanda, ProductComanda, StockMovement, StockMovementType

admin.site.register(Comanda)
admin.site.register(ProductComanda)
admin.site.register(StockMovementType)
admin.site.register(StockMovement)

