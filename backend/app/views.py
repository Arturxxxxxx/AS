from rest_framework import viewsets
from .models import Category
from .serializer import CategorySerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        # только категории верхнего уровня
        return Category.objects.filter(parent=None).prefetch_related('subcategories', 'products')

