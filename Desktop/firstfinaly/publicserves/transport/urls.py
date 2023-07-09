from django.urls import include, path
from transport import views

urlpatterns = [
    path('', views.TransportServesView.as_view()),
    path('review/', views.ReviewView.as_view()),
    path('companies/', views.TransportCompanyList.as_view()),
    path('companies/<int:pk>/', views.SingleTransportCompany.as_view()),
    path('trips/', views.TripsList.as_view()),
    path('trips/<int:pk>/', views.SingleTrip.as_view()),
    path('regtransport/', views.TransportCompanyRegisterAPIView.as_view()),
]
