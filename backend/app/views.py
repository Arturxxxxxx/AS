from google.cloud import translate_v2 as translate
from django.core.cache import cache
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Category
from .serializer import CategorySerializer

translate_client = translate.Client()

def translate_text(text, target_language='tr'):
    if not text:
        return text

    cache_key = f"{target_language}_{text}"
    cached_translation = cache.get(cache_key)
    if cached_translation:
        return cached_translation

    result = translate_client.translate(text, target_language=target_language)
    translated_text = result['translatedText']
    cache.set(cache_key, translated_text, timeout=60*60*24)
    return translated_text


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(parent=None).prefetch_related('subcategories', 'products')

    def list(self, request, *args, **kwargs):
        lang = request.GET.get('lang', 'ru')
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data

        if lang != 'ru':
            for category in data:
                self.translate_category(category, lang)

        return Response(data)

    def translate_category(self, category_data, lang):
        category_data['name'] = translate_text(category_data['name'], target_language=lang)

        for product in category_data['products']:
            product['name'] = translate_text(product['name'], target_language=lang)
            product['description'] = translate_text(product['description'], target_language=lang)

        for subcat in category_data['subcategories']:
            self.translate_category(subcat, lang)
