from django.db import models
from django.urls import reverse

class Vehicle(models.Model):
    title = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=0)
    mileage = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='vehicles/', blank=True, null=True) 

    created_at = models.DateTimeField(auto_now_add=True) 
    

    def __str__(self):
        return self.title
    
     
    def get_absolute_url(self):
        return reverse("vehicle_detail", args=[self.pk]) 

class VehicleImage(models.Model):
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='vehicles/')

    def __str__(self):
        return f"Image for {self.vehicle.title}"       

# Create your models here.
