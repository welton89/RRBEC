from django.db import models

# Create your models here.
class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    contact = models.CharField(max_length=255, null=True, blank=True)