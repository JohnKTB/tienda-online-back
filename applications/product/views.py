from rest_framework.generics import ListAPIView

from applications.product.models import Product
from applications.product.serializers import ProducstListSerializer


class ProductsListAPI(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProducstListSerializer


class FilterProductsAPI(ListAPIView):
    serializer_class = ProducstListSerializer

    def get_queryset(self):
        product = self.kwargs['product']
        return Product.objects.filter(name__icontains=product)[:10]
