import traceback
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Vehicle



def home(request):
    return render(request, 'home.html')


def vehicle_list(request):
    try:
        query = request.GET.get('q')

        if query:
            vehicles = Vehicle.objects.filter(
                Q(title__icontains=query) |
                Q(brand__icontains=query) |
                Q(description__icontains=query)
            )
        else:
            vehicles = Vehicle.objects.all()

        return render(request, 'vehicles/vehicle_list.html', {'vehicles': vehicles})

    except Exception as e:
        print("===== VEHICLE LIST ERROR =====")
        traceback.print_exc()
        raise e

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def vehicle_detail(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    return render(request, 'vehicles/vehicle_detail.html', {'vehicle': vehicle})