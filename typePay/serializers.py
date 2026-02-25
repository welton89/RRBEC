from rest_framework import serializers
from .models import TypePay

class TypePaySerializer(serializers.ModelSerializer):
    class Meta:
        model = TypePay
        fields = '__all__'
