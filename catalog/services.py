from .models import Product

def get_products_by_category(category_id):
    return Product.objects.filter(category_id=category_id)

from django.core.cache import cache
from .models import Product

def get_products_by_category_with_cache(category_id):
    cache_key = f'category_{category_id}'
    products = cache.get(cache_key)

    if not products:
        products = list(Product.objects.filter(category_id=category_id))
        cache.set(cache_key, products, timeout=60 * 15)  # Кеширование на 15 минут

    return products
