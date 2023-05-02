from django.urls import path
from .views import getRoutes, getData

urlpatterns = [
    path('', getRoutes, name="routes"),
    path('pharmacy/', getData, name="pharmacy Data"),
    path('pharmacy:pk>/', getData, name="one pharmacy"),
]
