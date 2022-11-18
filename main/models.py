from django.db import models


class Items(models.Model):
    title = models.CharField(max_length=100),
    brand = models.CharField(max_length=100),
    size =