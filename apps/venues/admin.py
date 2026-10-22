from django.contrib import admin

# Register your models here.
from .models import Venue

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display=("id", "name", "city", "capacity", "is_active", )
    list_filter=("city", "is_active")
    search_fields=("name", "description")
