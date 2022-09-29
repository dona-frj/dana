from django.contrib import admin
from .models import *


# Register your models here.

class meetupadmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('location',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(meetup, meetupadmin)
admin.site.register(Location)
admin.site.register(Participant)
