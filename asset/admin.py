from django.contrib import admin
from .models import Asset


class AssetAdmin(admin.ModelAdmin):
    list_display = ('host_name', 'host_group', 'host_cpu', 'host_memory', 'internal_ip', 'external_ip')
    list_filter = ('host_name',)
    list_editable = ('host_name', 'host_group', 'host_cpu', 'host_memory', 'internal_ip', 'external_ip')
    search_fields = ('host_name', 'host_group',)
    list_display_links = None


admin.site.register(Asset, AssetAdmin)
