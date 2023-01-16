from django.contrib import admin

from .models import Director, Genre, Films, FilmInstance

admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Films)
admin.site.register(FilmInstance)
