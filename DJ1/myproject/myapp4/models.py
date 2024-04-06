from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()
    image_us = models.ImageField(max_length=255, upload_to='images',
                                 default=None)  # upload_to='images' не срабатывает, пока непонятно почему

    def __str__(self):
        return f'Name: {self.name}, email: {self.email}, age: {self.age}'
