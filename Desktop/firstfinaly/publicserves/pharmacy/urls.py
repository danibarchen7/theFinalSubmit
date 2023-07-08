from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from pharmacy import views
from pharmacy.views import api_root
from rest_framework import renderers
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'users', views.UserViewSet,basename="user")
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })
urlpatterns = [
    # path('', views.api_root),
    path('pharmacy/', views.getPharmacyData, name="pharmacies Data"),
    path('pharmacy/<int:pk>/', views.getSinglePharmacy, name="one pharmacy"),
    path('pharmacyregister/', views.RegisterPharmacyAPIView.as_view()),
    # path('users/', user_list, name='user-list'),
    # path('users/<int:pk>/', user_detail, name='user-detail'),

]

