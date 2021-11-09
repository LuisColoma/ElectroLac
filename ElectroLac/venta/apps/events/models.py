from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=25, verbose_name='Nombre', unique=True)
    slug = models.SlugField(editable=False)
    summary = models.TextField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True)
    views = models.PositiveIntegerField(default=0)
    stock = models.IntegerField(default=0, verbose_name='Stock')
    Amount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio de venta')


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']


