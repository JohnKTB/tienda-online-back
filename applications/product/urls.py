from django.conf.urls.static import static
from django.urls import path

from applications.product.views import ProductsListAPI, FilterProductsAPI, CategoriesListAPI, \
    FilterProductsxCategoriesAPI
from bsale import settings

app_name = "product_app"

urlpatterns = [
    path('api/products/', ProductsListAPI.as_view(), name='products'),
    path('api/filter-product/<product>', FilterProductsAPI.as_view(), name='filter_product'),
    path('api/categories/', CategoriesListAPI.as_view(), name='categories'),
    path('api/filter-product-for-category/<category>', FilterProductsxCategoriesAPI.as_view(), name='filter_for_category'),
] + static(settings.local.MEDIA_URL, document_root=settings.local.MEDIA_ROOT)
