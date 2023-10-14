from rest_framework import *
from rest_framework import serializers
from .models import *
from tickets.models import *

from django.db.models.aggregates import *
from tickets.serializers import *


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'        


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['pk','reservation_guest', 'name', 'mobile']