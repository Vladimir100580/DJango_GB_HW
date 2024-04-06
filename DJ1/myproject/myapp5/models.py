from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # одна (категория) ко многим (продуктам)
    description = models.TextField(default='', blank=True)  # blank=True поле не обязательное для заполнения
    price = models.DecimalField(default=999999.99, max_digits=8, decimal_places=2)  # DecField т.к. Float - не точен
    quantity = models.PositiveSmallIntegerField(default=0)  # малое (до 2^15), положительное, целое число
    date_added = models.DateTimeField(auto_now_add=True)  # авто дата
    rating = models.DecimalField(default=5.0, max_digits=3, decimal_places=2)  # до 9.99 т.к. 3 цифры

    def __str__(self):
        return self.name
