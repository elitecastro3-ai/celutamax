from django.db import models

class Vehicle(models.Model):
    title = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    mileage = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='vehicles/')

    def __str__(self):
        return self.title

# Create your models here.
