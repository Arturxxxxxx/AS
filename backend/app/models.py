from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name="Категория")
    image = models.ImageField(upload_to='category/', verbose_name='фотография', null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')

    def __str__(self):
        return self.name


class ProductDessert(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=50, verbose_name='название')
    description = models.CharField(max_length=150, verbose_name='описание', null=True, blank=True)
    image = models.ImageField(upload_to='product/', verbose_name='фотография')
    size = models.CharField(max_length=50, verbose_name='размер')
    price = models.CharField(max_length=20, verbose_name='цена')
    currency = models.CharField(max_length=30, default='сом')

    def __str__(self):
        return self.name
