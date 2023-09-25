from django.db import models
from django.utils.text import slugify
from starts.models import Actor
from directors.models import Director
from taggit.managers import TaggableManager


class Movie(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date="release_date")
    image = models.URLField()
    genres = TaggableManager()
    description = models.TextField()
    release_year = models.PositiveIntegerField()
    release_date = models.DateField(auto_now=True)
    actors = models.ManyToManyField(Actor, related_name="movies")
    director = models.ManyToManyField(Director, related_name="movies")

    class Meta:
        ordering = ["-release_year"]

        indexes = [
            models.Index(
                fields=[
                    "-release_year"
                ]
            ),
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

        super().save(*args, **kwargs)
