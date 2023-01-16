from django.shortcuts import render
from .models import Director, Films, FilmInstance, Genre


def index(request):

    num_films = Films.objects.all().count()
    num_instances = FilmInstance.objects.all().count()
    num_director = Director.objects.all().count()

    disponibles = FilmInstance.objects.filter(status__exact="a").count()

    return render(
        request,
        "index.html",
        context={
            "num_films": num_films,
            "num_instances": num_instances,
            "num_director": num_director,
            "disponibles": disponibles
        }
    )
