from django.contrib import admin
from .models import meetup


# Register your models here.

class meetupadmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(meetup, meetupadmin)



