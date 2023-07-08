from django.urls import path, include
from mechanicals import views

urlpatterns = [
    path('mechanical/', views.MechanicalsList.as_view()),
    path('mechanical/<int:pk>/', views.getSingleMechanaicalData),
    path('mechanicalreg/', views.RegisterMechanicalAPIView.as_view())
]
