from django.contrib import admin
from app.models import ProductDessert, Category

admin.site.site_header = 'Администрация Эклат'
admin.site.site_title = 'Администрация Эклат'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # что показывать в списке

@admin.register(ProductDessert)
class ProductDessertAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
