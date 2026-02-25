from django.db import models

# Create your models here.
class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    debt = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    contact = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.name