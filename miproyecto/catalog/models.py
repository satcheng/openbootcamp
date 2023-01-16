import uuid
from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=64, help_text="Pon el nombre del género.")

    def __str__(self):
        return self.name


class Films(models.Model):
    title = models.CharField(max_length=32)
    director = models.ForeignKey("Director", on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=100, help_text="Pon de qué va la película")
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

    def getAbsoluteUrl(self):
        return reverse("film-detail", args=[str(self.id)])


class FilmInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para la película")
    film = models.ForeignKey("Films", on_delete=models.SET_NULL, null=True)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ("m", "Maintenance"),
        ("o", "On loan"),
        ("a", "Available"),
        ("r", "reserved")
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, help_text="Disponibilidad")

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        return "%s (%s)" % (self.id, self.film.title)


class Director(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    dateOfBirth = models.DateField(null=True, blank=True)
    dateOfDeath = models.DateField("Died", null=True, blank=True)

    def getAbsoluteUrl(self):
        return reverse("director-detail", args=[str(self.id)])

    def __str__(self):
        return "%s (%s)" % (self.lastName, self.firstName)
