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
    

    def __str__(self):
        return self.title
     
       
    created_at = models.DateTimeField(auto_now_add=True) 
    
    def get_absolute_url(self):
        return reverse("vehicle_detail", agr=[self.id])    

# Create your models here.
