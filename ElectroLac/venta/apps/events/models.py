from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(editable=False)
    summary = models.TextField(max_length=255)
    is_free = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    views = models.PositiveIntegerField(default=0)
    Amount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name
