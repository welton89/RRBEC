from django.contrib import admin

from products.models import Product, ProductComponent, UnitOfMeasure



admin.site.register(Product)
admin.site.register(ProductComponent)
admin.site.register(UnitOfMeasure)


