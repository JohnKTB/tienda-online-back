from django.db import models


class Category(models.Model):
    name = models.CharField('Nombre categoria', max_length=100, blank=True, default='')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'Category'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField('Nombre producto', max_length=70, blank=True, default='')
    url_image = models.ImageField('Imagen Producto', blank=True, null=True, upload_to='products')
    price = models.FloatField('Precio de Venta', null=True)
    discount = models.IntegerField('Descuento producto', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        db_table = 'product'

    def __str__(self):
        return self.name
