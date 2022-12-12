from django.db import models
from django.urls import reverse




class Shirts(models.Model):

    name = models.CharField(max_length=100, default='none')
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='Shirts', null=True, verbose_name='Изображение')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')
