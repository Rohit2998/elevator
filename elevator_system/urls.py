from django.urls import include, path

from rest_framework import routers

from elevator_system.views import ElevatorViewSet

router = routers.DefaultRouter()
router.register(r'elevator', ElevatorViewSet)

urlpatterns = [
   path('', include(router.urls)),
]