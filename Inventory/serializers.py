from rest_framework import serializers
from .models import Products

class Products_Serializer(serializers.ModelSerializer): 
    class Meta:
        model = Products
        fields = '__all__'

class Products_Serializer1(serializers.ModelSerializer): 
    class Meta:
        model = Products
        fields = ['product_name']
