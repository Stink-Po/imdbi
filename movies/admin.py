from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'genres', 'release_year']
    list_filter = ['release_year', 'genres']
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "release_date"
    ordering = ['release_year', 'title']
