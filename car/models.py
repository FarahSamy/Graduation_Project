from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


# Create your models here.
class Signup(models.Model):
    username = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    phone = models.IntegerField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.Email


class Owner(models.Model):
    FN_owner = models.CharField(max_length=50, null=True, blank=True)
    LN_owner = models.CharField(max_length=50, null=True, blank=True)
    phone_owner = models.IntegerField(null=True, blank=True)
    usedCar_city = models.CharField(max_length=50, null=True, blank=True)
    email_owner = models.CharField(max_length=50, null=True, blank=True)
    nearestLocation = models.CharField(max_length=50, null=True, blank=True)


class Car(models.Model):
    transmission = [
        ('manual', 'Manual'),
        ('automatic', 'Automatic')
    ]
    cy = [
        ('4', '4'),
        ('6', '6'),
        ('8', '8'),
    ]

    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    power = models.CharField(max_length=50)
    Price = models.DecimalField(max_digits=9, decimal_places=2)
    transmission_type = models.CharField(max_length=50, choices=transmission)
    body_style = models.CharField(max_length=50, null=True, blank=True)
    cylinder = models.IntegerField(choices=cy, null=True, blank=True)
    doors = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='photos/%y/%m/%d', null=True, blank=True)
    engine_size = models.IntegerField()
    owner_car = models.ForeignKey(Owner, on_delete=models.CASCADE, blank=True, default='')

    def __str__(self):
        return self.name

