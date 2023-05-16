from django.db import models
from datetime import datetime

# Create your models here.
class Signup(models.Model):
    userName = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    phone = models.IntegerField()
    password = models.CharField(max_length=50)


class Car(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.DateTimeField()
    power = models.CharField(max_length=50)
    Price = models.DecimalField(max_digits=9, decimal_places=2)
    transmission_type = models.CharField(max_length=50)
    body_style = models.CharField(max_length=50)
    cylinder = models.IntegerField()
    doors = models.IntegerField()
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    engine_size = models.IntegerField()


