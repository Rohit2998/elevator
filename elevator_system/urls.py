from django.urls import path

from .views import *

urlpatterns=[

    path('el-sys/list/',ElevatorSystemList.as_view(),name='el-sys-list'),
    path('el-sys/add-new/',CreateElevatorSystem.as_view(),name='add-new-els'),
    path('el-sys/<int:id>/list/',ElevatorsList.as_view(),name='elevator-list'),
    path('el-sys/<int:id>/elevator/<int:pk>/view/',ViewSingleElevator.as_view(),name='elevator-view'),
    path('el-sys/<int:id>/elevator/<int:pk>/update/',UpdateSingleElevator.as_view(),name='elevator-update'),
    path('el-sys/<int:id>/elevator/<int:pk>/destination/',FetchDestination.as_view(),name='fetch-destination'),
    path('el-sys/<int:id>/elevator/<int:pk>/req/add-new/',CreateElevatorRequest.as_view(),name='add-new-req'),
    path('el-sys/<int:id>/elevator/<int:pk>/req/view/',ElevatorRequestList.as_view(),name='req-list'),
]