from django.shortcuts import render
from .models import Movie
from directors.models import Director
from starts.models import Actor
from user.models import CustomUser
from django.views.generic import ListView
import pandas as pd
from django.http.response import HttpResponse
from festivals.models import Festival


# class MovieList(ListView):
#    model = Movie
#    template_name = 'index.html'
#   paginate_by = 12

def lists_done(request):
    names = ['Festival Name', 'Website', 'Start Date', 'End Date', 'City']
    df = pd.read_csv("2020 Film Festival Database & Calendar - 2020 DATABASE.csv", usecols=names)
    clean_df = df[df["Start Date"] != 'tbd']
    for index, row in clean_df.iterrows():
        festival_name = row['Festival Name']
        site = row['Website']
        city = row['City']
        start_month, start_day = row['Start Date'].replace("`", "").split("/")[0:2]
        start_month = start_month.zfill(2)
        start_day = start_day.zfill(2)
        end_month, end_day = row['End Date'].replace("`", "").split("/")[0:2]
        end_month = end_month.zfill(2)
        end_day = end_day.zfill(2)
        start_date = start_month + "-" + start_day
        end_date = end_month + "-" + end_day
        new_fest = Festival(name=festival_name,
                            city=city,
                            url=site,
                            start=start_date,
                            end=end_date)
        new_fest.save()
    return HttpResponse("<h1>done</h1>")
