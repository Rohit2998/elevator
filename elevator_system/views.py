from django.shortcuts import render
from elevator_system.models import Elevator
from elevator_system.serializers import ElevatorSerializer
from rest_framework import viewsets
from rest_framework import viewsets 
from rest_framework import viewsets

# Create your views here.
class ElevatorViewSet(viewsets.ViewSet):
    queryset=Elevator.objects.all()
    serializer_class=ElevatorSerializer
