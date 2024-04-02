from django.db import models


class ProductCard(models.Model):
    image = models.CharField(max_length=200)
    item_name = models.CharField(max_length=200)
    cost = models.CharField(max_length=200)
    info = models.CharField(max_length=200)
