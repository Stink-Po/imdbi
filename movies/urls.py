from django.urls import path
from . import views

app_name = "movie"

urlpatterns = [
    #path("", views.MovieList.as_view(), name="index"),
    path("", views.lists_done, name="index")
]
