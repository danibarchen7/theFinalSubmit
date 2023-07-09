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
class SingleTransportCompany(APIView):
    def get (self,request,pk):
        transport = TransportsCompany.objects.get(ip_tc=pk)
        serializer = TransportsCompanySerializer(transport, many=False)
        return Response(serializer.data)
    def delete(self,request,pk):
      transport = TransportsCompanySerializer.objects.get(ip_tc=pk)
      transport.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):

        transport = TransportsCompany.objects.get(ip_tc=pk)
        serializer = TransportsCompanySerializer(transport, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class TransportCompanyList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = TransportsCompany.objects.all()
    serializer_class = TransportsCompanySerializer
    
# add trip
class SingleTrip(APIView):
    def get (self,request,pk):
        trip = Trips.objects.get(ip_t=pk)
        serializer = TripsSerializer(trip, many=False)
        return Response(serializer.data)
    def delete(self,request,pk):
      trips = Trips.objects.get(ip_t=pk)
      trips.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):

        trip = Trips.objects.get(ip_t=pk)
        serializer = TripsSerializer(trip, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class TripsList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Trips.objects.all()
    serializer_class = TripsSerializer
    

    
# display the service


class TransportServesView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = TransportService.objects.all()
    serializer_class = TransportServesSerializer

class ReviewView(APIView):
    serializer_class = ReviewSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
