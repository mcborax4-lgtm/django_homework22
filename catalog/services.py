from django.core.cache import cache
from .models import Product


def get_products_by_category(category_id):
    return Product.objects.filter(category_id=category_id)


def get_cached_products():
    products = cache.get('products_list')
    if products is None:
        products = list(Product.objects.all())
        cache.set('products_list', products, 60)
    return products