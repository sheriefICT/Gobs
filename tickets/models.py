from django.db import models
from django.utils import timezone


class Movie(models.Model):
    hall = models.CharField(max_length=10)
    movie  = models.CharField(max_length=10)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.hall

class Guest(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=12)
    def __str__(self):
        return self.name


class Reservation(models.Model):
    guest = models.ForeignKey( Guest, related_name='reservation_guest', on_delete=models.CASCADE)
    movie = models.ForeignKey( Movie, related_name='reservation_movie', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.guest)