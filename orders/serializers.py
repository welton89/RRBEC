from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    product_name = serializers.ReadOnlyField(source='id_product.name')
    comanda_name = serializers.ReadOnlyField(source='id_comanda.name')
    mesa_name = serializers.ReadOnlyField(source='id_comanda.mesa.name')

    class Meta:
        model = Order
        fields = [
            'id', 'id_product', 'product_name', 'id_comanda', 'comanda_name', 
            'mesa_name', 'obs', 'queue', 'preparing', 'finished', 
            'delivered', 'canceled', 'status'
        ]
        extra_kwargs = {
            'queue': {'read_only': True},
            'status': {'read_only': True},
        }

    def get_status(self, obj):
        if obj.delivered:
            return 'Entregue'
        if obj.finished:
            return 'Pronto'
        if obj.preparing:
            return 'Preparando'
        if obj.canceled:
            return 'Cancelado'
        return 'Em espera'
