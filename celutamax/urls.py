from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from vehicles.views import home, vehicle_list, vehicle_detail, about, contact
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from vehicles.models import Vehicle


sitemaps = {
    "vehicles": GenericSitemap({
        "queryset": Vehicle.objects.all(),
        "date_field": "created_at"
     })   
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path("sitemap.xml", sitemap,{"sitemaps":sitemaps}, name="sitemap"),
    path('', home, name='home'),   # Homepage
    path('vehicles/', vehicle_list, name='vehicles'),
    path('vehicles/<int:pk>/', vehicle_detail, name='vehicle_detail'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static files in development (optional, since Whitenoise handles it in production)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)