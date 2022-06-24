from django.contrib import admin
from .models import Event


class AdminEvents(admin.ModelAdmin):
    list_display = (
        'event_name',
        'date',
        'location',
    )
    ordering = ('-date',)


admin.site.register(Event, AdminEvents)
