from django.db.models.signals import post_save, post_delete
from .models import ChangeLog

from products.models import Product
from comandas.models import Comanda, ProductComanda
from orders.models import Order
from clients.models import Client
from categories.models import Categories
from mesas.models import Mesa
from payments.models import Payments

MODELS_TO_TRACK = [
    Product, Comanda, ProductComanda, Order, Client, Categories, Mesa, Payments
]

def handle_save(sender, instance, created, **kwargs):
    model_name = sender.__name__
    ChangeLog.objects.create(
        model_name=model_name,
        object_id=instance.id,
        action='SAVE'
    )

def handle_delete(sender, instance, **kwargs):
    model_name = sender.__name__
    ChangeLog.objects.create(
        model_name=model_name,
        object_id=instance.id,
        action='DELETE'
    )

def register_signals():
    for model in MODELS_TO_TRACK:
        post_save.connect(handle_save, sender=model, dispatch_uid=f"sync_save_{model.__name__}")
        post_delete.connect(handle_delete, sender=model, dispatch_uid=f"sync_delete_{model.__name__}")
