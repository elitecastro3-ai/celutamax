from django.contrib.sitemaps import Sitemap
from .models import Vehicle


class VehicleSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Vehicle.objects.filter(id__isnull=False)

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        try:
            return obj.get_absolute_url()
        except:
            return "/"