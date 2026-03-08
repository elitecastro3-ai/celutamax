from django.contrib.sitemaps import Sitemap
from .models import Vehicle


class VehicleSitemap(Sitemap):
    

    def items(self):
        return Vehicle.objects.all()

   