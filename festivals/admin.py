from django.contrib import admin
from .models import Festival


@admin.register(Festival)
class FestivalAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'start', 'end', 'city', 'url']
    list_filter = ['city']
    search_fields = ['title', 'city']
    prepopulated_fields = {'slug': ('title',)}

