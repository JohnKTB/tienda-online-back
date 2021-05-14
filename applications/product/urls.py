from django.conf.urls.static import static
from django.urls import path

from applications.product.views import ProductsListAPI, FilterProductsAPI
from bsale import settings

app_name = "product_app"

urlpatterns = [
    path('api/products/', ProductsListAPI.as_view(), name='products'),
    path('api/filter-product/<product>', FilterProductsAPI.as_view(), name='filter_product'),
] + static(settings.local.MEDIA_URL, document_root=settings.local.MEDIA_ROOT)
