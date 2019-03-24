from django.contrib import admin
from .models import Event, EventImage

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    search_fields = ['title', 'description']
    list_display = [ 'title', 'price', 'active', 'updated']
    list_editable = ['price', 'active']
    list_filter = ['price', 'active']
    readonly_fields = ['timestamp', 'updated']
    prepopulated_fields = {'slug': ('title',)}
    class Meta:
        model = Event

admin.site.register(Event, EventAdmin)
admin.site.register(EventImage)
