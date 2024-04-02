from rest_framework import serializers
from .models import ProductCard


class ProductCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCard
        fields = ['image', 'item_name', 'cost', 'info']
