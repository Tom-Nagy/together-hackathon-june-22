from django.contrib import admin
from .models import Event

# Register your models here.

class AdminEvents(admin.ModelAdmin):
    list_display = (
        'event_name',
        'date',
        'location',
    )
    ordering= ('-date',)


admin.site.register(Event, AdminEvents)
