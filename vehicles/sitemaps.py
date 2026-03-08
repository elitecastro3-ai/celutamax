from django.contrib.sitemaps import Sitemap
from .models import Vehicle


class VehicleSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return Vehicle.objects.all()

    def lastmod(self, obj):
        return obj.created_at