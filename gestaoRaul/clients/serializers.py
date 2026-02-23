from rest_framework import serializers
from .models import Client
from comandas.models import Comanda, ProductComanda
from payments.models import Payments, somar
from decimal import Decimal

class ClientSerializer(serializers.ModelSerializer):
    debt = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ['id', 'name', 'created_at', 'active', 'contact', 'debt']

    def get_debt(self, obj):
        comandas = Comanda.objects.filter(client=obj, status='FIADO')
        total_debt = Decimal(0)
        
        for comanda in comandas:
            consumo = ProductComanda.objects.filter(comanda=comanda)
            valores = somar(consumo, comanda)
            total_debt += valores['totalSemTaxa']
            
        return total_debt
