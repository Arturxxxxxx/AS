from rest_framework import serializers
from .models import Category, ProductDessert

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductDessert
        fields = ['id', 'name', 'description', 'image', 'price', 'currency', 'size']

class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.SerializerMethodField()
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'subcategories', 'products']

    def get_subcategories(self, obj):
        # рекурсивно сериализуем подкатегории
        sub_qs = obj.subcategories.all()
        return CategorySerializer(sub_qs, many=True, context=self.context).data
