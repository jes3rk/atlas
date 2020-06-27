from django.db import models

class Address(models.Model):
    house_number = models.CharField(max_length=128)
    street = models.CharField(max_length=128)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=5)
    latitude = models.FloatField()
    longitude = models.FloatField()