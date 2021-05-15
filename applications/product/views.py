from rest_framework.generics import ListAPIView

from applications.product.models import Product, Category
from applications.product.serializers import ProducstListSerializer, CategoryListSerializer


class ProductsListAPI(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProducstListSerializer


class FilterProductsAPI(ListAPIView):
    serializer_class = ProducstListSerializer

    def get_queryset(self):
        product = self.kwargs['product']
        return Product.objects.filter(name__icontains=product)[:10]


class CategoriesListAPI(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class FilterProductsxCategoriesAPI(ListAPIView):
    serializer_class = ProducstListSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return Product.objects.filter(category=category)[:10]
