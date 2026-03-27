from django.contrib import admin
from django.utils.html import mark_safe
from .models import Vehicle, VehicleImage


# ✅ Inline for multiple images
class VehicleImageInline(admin.TabularInline):
    model = VehicleImage
    extra = 3


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'price', 'year')
    readonly_fields = ('image_preview',)

    # 👇 Add inline images
    inlines = [VehicleImageInline]

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="150"/>')
        return "(No image)"