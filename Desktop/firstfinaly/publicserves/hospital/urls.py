from django.urls import path, include
from hospital import views

urlpatterns = [
    path('regester/', views.RegisterHospitalAPIView.as_view()),
    path('review/', views.ReviewView.as_view()),
    path('hospitalserviec/', views.HospitalServesViewList.as_view()),
    path('', views.HospitalsList.as_view()),
    path('<int:pk>/',
         views.SingleHospitalView.as_view(), name="sigle hospital"),
]
