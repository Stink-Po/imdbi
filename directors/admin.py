from django.contrib import admin
from .models import Director


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['name','display_movies']
    search_fields = ['name']
    ordering = ["name"]

    def display_movies(self, obj):
        return ", ".join([movie.title for movie in obj.movies.all()])

    display_movies.short_description = "Movies"

