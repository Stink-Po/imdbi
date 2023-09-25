from django.db import models


class Festival(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    start = models.CharField(max_length=50)
    end = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title
