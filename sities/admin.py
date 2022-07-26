from django.contrib import admin

from sities.models import City


@admin.register(City)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
