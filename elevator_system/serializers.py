from rest_framework import serializers
from elevator_system.models import *

class ElevatorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Elevator
        fields=('elevatorID','currentfloor','requested_floor','elevator_status')
