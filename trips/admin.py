from django.contrib import admin

from .models import Trip


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ("title", "destination", "start_date", "end_date", "owner")
    search_fields = ("title", "destination", "owner__username")
    list_filter = ("start_date", "end_date")
