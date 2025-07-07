from django.db import models

from categories.models import Categories


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

    def __str__(self) -> str:
        return f"{self.id} - {self.name} - {self.price} - {self.category} - {self.cuisine} - {self.active} "
