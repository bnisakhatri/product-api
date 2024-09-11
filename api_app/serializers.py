from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'parent']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # Nesting CategorySerializer to include category details

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'price', 'image', 'description', 'created_at', 'updated_at']
