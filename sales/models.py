from django.db import models
from datetime import date

class ProductDetails(models.Model):
    urbanizacion = models.CharField(max_length=90)

    def __str__(self):
        return self.urbanizacion

class SalesDetails(models.Model):
    urbanizacion = models.CharField(max_length=90)
    fecha = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    p_id = models.IntegerField(null=True)
    def __str__(self):
        return self.urbanizacion

class RegistrationDetails(models.Model):
    username = models.CharField(max_length=60)
    email = models.EmailField()
    password = models.CharField(max_length=16)

    def __str__(self):
        return self.username