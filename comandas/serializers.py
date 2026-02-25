from rest_framework import serializers
from .models import Comanda, ProductComanda

class ProductComandaSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')
    obs = serializers.SerializerMethodField()

    class Meta:
        model = ProductComanda
        fields = ['id', 'comanda', 'data_time', 'product', 'product_name', 'applicant', 'obs']

    def get_obs(self, obj):
        order = obj.order_set.first()
        return order.obs if order else ""

class ComandaSerializer(serializers.ModelSerializer):
    mesa_name = serializers.ReadOnlyField(source='mesa.name')
    client_name = serializers.ReadOnlyField(source='client.name')
    user_name = serializers.ReadOnlyField(source='user.username')
    items = ProductComandaSerializer(many=True, read_only=True, source='productcomanda_set')

    class Meta:
        model = Comanda
        fields = [
            'id', 'mesa', 'mesa_name', 'user', 'user_name', 
            'type_pay', 'dt_open', 'dt_close', 'client', 
            'client_name', 'name', 'status', 'items'
        ]
