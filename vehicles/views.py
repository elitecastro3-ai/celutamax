from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
from django.shortcuts import render    
from .models import Vehicle

def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicles.html', {'vehicles': vehicles})
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')