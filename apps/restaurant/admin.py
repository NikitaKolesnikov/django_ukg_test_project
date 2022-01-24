from django.contrib import admin

from apps.restaurant.models import Restaurant


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Restaurant, RestaurantAdmin)
