from django.db import models
from django.contrib.auth.models import User

from categories.models import Categories
# from comandas.models import Comanda



class UnitOfMeasure(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True, help_text="Ex: 'Unidade', 'Kg', 'Litro'")
    abbreviation = models.CharField(max_length=10, unique=True, help_text="Ex: 'un', 'kg', 'L'")

    def __str__(self):
        return self.abbreviation


# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(null=False, default=0)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    cuisine = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    unit_of_measure = models.ForeignKey(
        UnitOfMeasure,
        on_delete=models.SET_NULL, # Define como NULL se a unidade de medida for excluída
        null=True,
        blank=True,
        help_text="Unidade de medida para este produto."
    )

    # Campo de composição (mantido da resposta anterior)
    components = models.ManyToManyField(
        'self',
        through='ProductComponent',
        through_fields=('composite_product', 'component_product'),
        symmetrical=False,
        related_name='is_component_of'
    )


    def __str__(self) -> str:
        return f"{self.name}"

    def subStock(self, qtd):
        self.quantity -= qtd
        self.save()

    def addStock(self, qtd):
        self.quantity += qtd
        self.save()



class ProductComponent(models.Model):
    composite_product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='composition_entries',
        help_text="O produto que é composto por outros produtos."
    )
    component_product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='used_as_component_in',
        help_text="Um produto que é componente de outro produto."
    )
    quantity_required = models.PositiveIntegerField(
        default=1,
        help_text="Quantidade deste componente necessária para o produto composto."
    )

    class Meta:
        unique_together = ('composite_product', 'component_product')

    def __str__(self):
        return (
            f"{self.composite_product.name} requer "
            f"{self.quantity_required} de {self.component_product.name}"
        )




