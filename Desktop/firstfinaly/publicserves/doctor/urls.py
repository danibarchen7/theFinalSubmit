from django.urls import path, include
from doctor import views

app_name = 'doctor'

urlpatterns = [
    path('doctorsrigester/', views.RegisterDoctorAPIView.as_view()),
    # path('doctorsrigester/rigesterspechializetion',
    #      views.RegisterSpecializationAPIView.as_view()),
    path('', views.DoctorsList.as_view()),
    path('doctorslist/<int:pk>/', views.getSingleDoctorData, name="doctor"),
    # path('login/', views.DoctorLoginView.as_view()),
    # path('<id>/update', views.update_view),
    # path('doctor/', views.AddDoctorView.as_view(), name="add"),
]
