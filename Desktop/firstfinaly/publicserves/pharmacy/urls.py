from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from pharmacy import views
from rest_framework import renderers

urlpatterns = [
    path('', views.PharmacyListView.as_view(), name="pharmacies Data"),
    path('review/', views.ReviewView.as_view(), name="pharmacies Data"),
    path('medicen/',views.MedicenList.as_view()),
    path('medicen/<int:pk>',views.SingleMedicenView.as_view()),
    path('<int:pk>/', views.SinglePharmacy.as_view(), name="one pharmacy"),
    path('pharmacyregister/', views.RegisterPharmacyAPIView.as_view()),

]

