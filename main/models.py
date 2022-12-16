from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class SizeVariant(models.Model):
    size_name = models.CharField(max_length=6, null=True)

    def __str__(self):
        return self.size_name


class Item(models.Model):
    title = models.CharField(max_length=100, default='какая-то кепка')
    image = models.ImageField(upload_to='static/main', blank=True, null=True)
    description = models.TextField(default='описание какой-то кепке')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    size = models.ForeignKey(SizeVariant, on_delete=models.PROTECT, null=True)
    count = models.PositiveIntegerField()

    def __str__(self):
        return self.title


