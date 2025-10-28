from rest_framework import viewsets
from .models import Category
from .serializer import CategorySerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.prefetch_related('subcategories', 'products')
    serializer_class = CategorySerializer