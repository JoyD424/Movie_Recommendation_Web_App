# Generated by Django 2.2 on 2019-05-20 00:09
from django.db import migrations, models
import io
import os

currentDir = os.path.dirname(__file__)
parentDir = os.path.split(currentDir)[0]
urlsPath = os.path.join(parentDir, 'urlsList.txt')


def addURLsToAllMovies(apps, schema_editor):
    Movie = apps.get_model("movieRecommendation", "Movie")

    f = io.open(urlsPath, 'r', encoding='latin1')
    urls = [line.strip().split("::") for line in f.readlines()]
    for lst in urls:
        id = int(lst[0])
        movie = Movie.objects.get(movieID = id)
        movie.moviePosterURL = lst[1]
        movie.movieBackdropURL = lst[2]
        movie.save()

    

def deleteURLs(apps, schema_editor):
    Movie = apps.get_model("movieRecommendation", "Movie")
    allMovies = Movie.objects.all()
    for movie in allMovies:
        movie.moviePosterURL = ''
        movie.movieBackdropURL = ''
        movie.save()
        


class Migration(migrations.Migration):

    dependencies = [
        ('movieRecommendation', '0004_auto_20190519_2303'),
    ]

    operations = [
        migrations.RunPython(addURLsToAllMovies, reverse_code=deleteURLs),
    ]