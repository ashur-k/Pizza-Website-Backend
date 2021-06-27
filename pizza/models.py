from django.db import models
from django.contrib.postgres.fields import ArrayField
from rest_framework import serializers


class Pizza(models.Model):
  
  name = models.CharField(max_length=200)
  slug = models.SlugField()
  description = models.CharField(max_length=500)
  toppings = ArrayField(
    models.CharField(max_length=200)
    )
  image = models.URLField()
  price = models.FloatField()
  
  class Meta:
    verbose_name_plural = 'Pizzas'
    ordering = ['name', ]
  
  def __str__(self):
    return self.name

