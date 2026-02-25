from rest_framework import serializers
from .models import Product, UnitOfMeasure

class UnitOfMeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitOfMeasure
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    unit_of_measure_name = serializers.ReadOnlyField(source='unit_of_measure.name')

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'image', 'price', 
            'quantity', 'category', 'category_name', 
            'cuisine', 'active', 'unit_of_measure', 'unit_of_measure_name'
        ]
