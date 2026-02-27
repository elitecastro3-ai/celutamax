from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from vehicles.views import home, vehicle_list, vehicle_detail, about, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),   # THIS is the homepage
    path('vehicles/', vehicle_list, name='vehicles'),
    path('vehicles/<int:pk>/', vehicle_detail, name='vehicle_detail'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)