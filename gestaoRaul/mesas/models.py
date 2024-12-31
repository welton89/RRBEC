from django.db import models



class Mesa(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255, null=True, blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    # Foreign Key to Comandas model (assuming it exists)
    # comanda = models.ForeignKey('Comandas', on_delete=models.DO_NOTHING, db_column='id_mesa')