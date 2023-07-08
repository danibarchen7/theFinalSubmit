from django.urls import include, path
from transport import views

urlpatterns = [
    path('', views.TransportServesView.as_view()),
    path('companies/', views.TransportCompanyList.as_view()),
    path('trips/', views.TripsList.as_view()),
    path('<int:pk>/', views.getSingleTransportCompanyData),
    path('regtransport/', views.TransportCompanyRegisterAPIView.as_view()),
]
