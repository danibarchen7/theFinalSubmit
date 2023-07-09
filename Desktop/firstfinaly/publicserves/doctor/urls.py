from django.urls import path, include
from doctor import views

app_name = 'doctor'

urlpatterns = [
    path('doctorsrigester/', views.RegisterDoctorAPIView.as_view()),
    # path('doctorsrigester/rigesterspechializetion',
    #      views.RegisterSpecializationAPIView.as_view()),
    path('', views.DoctorsList.as_view()),
    path('<int:pk>/', views.SingleDoctorView.as_view(), name="doctor"),
    path('review/', views.ReviewView.as_view()),

]
