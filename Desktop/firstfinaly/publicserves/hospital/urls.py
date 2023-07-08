from django.urls import path, include
from hospital import views

urlpatterns = [
    path('', views.RegisterHospitalAPIView.as_view()),
    path('hospitalserviec/', views.HospitalServesViewList.as_view()),
    path('hospitallist/', views.HospitalsList.as_view()),
    path('hospitallist/<int:pk>/',
         views.getSingleHospitalsData, name="sigle hospital"),
]
