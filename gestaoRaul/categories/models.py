from django.db import models

# Create your models here.
class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


    def __str__(self) -> str:
        return self.name