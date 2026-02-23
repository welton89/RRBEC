from rest_framework import serializers
from .models import Payments

class PaymentsSerializer(serializers.ModelSerializer):
    type_pay_name = serializers.ReadOnlyField(source='type_pay.name')
    comanda_name = serializers.ReadOnlyField(source='comanda.name')
    client_name = serializers.ReadOnlyField(source='client.name')

    class Meta:
        model = Payments
        fields = [
            'id', 'value', 'type_pay', 'type_pay_name', 
            'comanda', 'comanda_name', 'client', 'client_name', 
            'description', 'datetime'
        ]
