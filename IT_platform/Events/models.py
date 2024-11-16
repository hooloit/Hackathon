from django.db import models
from django.db.models import Model
from typing_extensions import ReadOnly


class Event(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=50)
    special = models.CharField(max_length=100)
    place = models.CharField()
    description = models.CharField()
    date = models.DateField()
    organizer = models.CharField()
    image = models.ImageField(upload_to='image/avatar/')

    def __str__(self):
        return self.title


class User(models.Model):
    username = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=80)
    second_name = models.CharField(max_length=80)
    surname = models.CharField(max_length=80)
    birth = models.DateField()
    category = models.CharField(max_length=100)
    special = models.CharField(max_length=100)
    github = models.URLField()
    portfolio = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='image/event/')