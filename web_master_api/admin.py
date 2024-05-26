from django.contrib import admin

from .models import ConfigDetail, MenuItem, WebsiteDetail


@admin.register(WebsiteDetail)
class WebsiteDetailAdmin(admin.ModelAdmin):
    list_display = ('title', 'web_url', 'feature', 'created_at', 'updated_at')

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'order', 'is_visible', 'created_at', 'updated_at')

@admin.register(ConfigDetail)
class ConnfigDetailsAdmin(admin.ModelAdmin):
    list_display = ('config_type', 'created_at', 'updated_at')
    