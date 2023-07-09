from django.urls import path, include
from mechanicals import views

urlpatterns = [
    path('', views.MechanicalsList.as_view()),
    path('typevichale/', views.TypeVechaleList.as_view()),
    path('typevichale/<int:pk>', views.SingleTypeVechaleView.as_view()),
    path('<int:pk>/', views.SingleMechanicalView.as_view()),
    path('mechanicalreg/', views.RegisterMechanicalAPIView.as_view()),
    path('review/', views.ReviewView.as_view())
]
