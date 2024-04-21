from typing import Any
from django.db import models

# Create your models here.


VOLTAGE_LEVELS = (
    ("12~48", "12~48"),
    ("110", "110"),
    ("220", "220"),
    ("110 ~ 240", "110 ~ 240"),
    ("415", "415"),
    ("N/A", "N/A"),
)

VOLTAGE_TYPE = (
    ("AC", "AC"),
    ("DC", "DC"),
    ("AC & DC", "AC & DC"),
    ("N/A", "N/A"),
)

PHASES = (
    ("3-PHASE", "3-PHASE"),
    ("1-PHASE", "1-PHASE"),
    ("1 & 3 PHASE", "1 & 3 PHASE"),
    ("N/A", "N/A"),
)


class Category(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Category - {self.name}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100, null=True)
    category = models.ManyToManyField(Category)
    voltage_level = models.CharField(choices=VOLTAGE_LEVELS, max_length=20)
    voltage_type = models.CharField(choices=VOLTAGE_TYPE, max_length=10)
    phases = models.CharField(choices=PHASES, max_length=20)
    power = models.IntegerField()
    price = models.IntegerField()
    featured_product = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    description = models.TextField(max_length=500, null=True)
    photo = models.ImageField(upload_to="images/store/products_main", null=True)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}-{self.category}"


class ProductImages(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to="images/store/product")

    def __str__(self) -> str:
        return f"{self.product.name}"
