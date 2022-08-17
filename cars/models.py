from django.db import models


class Driver(models.Model):
    name = models.TextField()
    license = models.TextField()


class Car(models.Model):
    make = models.TextField()
    model = models.TextField()
    year = models.IntegerField()
    vin = models.TextField()  # VIN stands for: Vehicle Identification Number
    owner = models.ForeignKey("Driver", on_delete=models.SET_NULL, null=True)
