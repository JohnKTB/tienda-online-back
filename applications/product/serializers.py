from rest_framework import serializers

from applications.product.models import Product, Category
from bsale.settings.local import MEDIA_URL


# CATEGORIES
class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name'
        )


# PRODUCTS
class ProducstListSerializer(serializers.ModelSerializer):
    url_image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'url_image',
            'price',
            'discount'
        )

    def get_url_image(self, instance):
        image = f'http://127.0.0.1:8000{MEDIA_URL}{instance.url_image}'
        return image
