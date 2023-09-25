from django.contrib import admin
from .models import Actor


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['name', 'display_movies']

    def display_movies(self, obj):
        return ", ".join([movie.title for movie in obj.movies.all()])

    display_movies.short_description = 'Movies'
