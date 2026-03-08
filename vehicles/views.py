from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Vehicle


def home(request):
    return render(request, 'home.html')


def vehicle_list(request):
    query = request.GET.get('q')

    vehicles = Vehicle.objects.all()

    if query:
        vehicles = vehicles.filter(
            Q(title__icontains=query) |
            Q(brand__icontains=query) |
            Q(description__icontains=query)
        )

    return render(request, 'vehicles/vehicle_list.html', {'vehicles': vehicles})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def vehicle_detail(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    return render(request, 'vehicles/vehicle_detail.html', {'vehicle': vehicle})