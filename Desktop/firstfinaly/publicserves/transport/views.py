from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from .models import TransportsCompany, Trips
from .serializers import *
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
# Create your views here.
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

# get the info of one transport company


@api_view(['GET'])
def getSingleTransportCompanyData(request, pk):
    mechanical = TransportsCompany.objects.get(ip_tc=pk)
    serializer = TransportsCompanySerializer(mechanical, many=False)
    return Response(serializer.data)

# add data or update date to the transport company


class TransportCompanyRegisterAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = TransportRegisterSerializer

# transport company list


class TransportCompanyList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = TransportsCompany.objects.all()
    serializer_class = TransportsCompanyListSerializer

# add trip


class TripsList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Trips.objects.all()
    serializer_class = TripsSerializer


# display the service


class TransportServesView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = TransportService.objects.all()
    serializer_class = TransportServesSerializer
