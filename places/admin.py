from django.contrib import admin
from django.utils.html import format_html

from adminsortable2.admin import SortableInlineAdminMixin

from .models import Place, PlaceImage


class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    readonly_fields = ['place_image_preview']

    def place_image_preview(self, obj):
        return format_html('<img src="{}" style="max-width:{}px;max-height:{}px">', obj.image.url, 200, 150)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        PlaceImageInline
    ]
