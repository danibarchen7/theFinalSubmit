from django.urls import path
from .views import getRoutes, getData, getSingleData

urlpatterns = [
    path('', getRoutes, name="routes"),
    path('pharmacy/', getData, name="pharmacy Data"),
    path('pharmacy/<int:pk>/', getSingleData, name="one pharmacy"),
]
