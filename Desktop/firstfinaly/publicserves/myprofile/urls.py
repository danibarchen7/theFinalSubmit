from django.urls import path, include
from myprofile import views
from rest_framework.authtoken.views import obtain_auth_token
from knox import views as knox_views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
app_name = 'myprofile'
urlpatterns = [
    path('login/', views.LoginView.as_view(),
         name='token_obtain_pair'),

    path('<int:pk>/', views.MyProfileView.as_view()),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('register/', views.RegisterUserAPIView.as_view()),
    path('logout/', views.LogoutView.as_view(), name="logout")
]
