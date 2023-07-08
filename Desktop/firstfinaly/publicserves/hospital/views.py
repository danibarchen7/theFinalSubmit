from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import HospitalRegisterSerializer, HospitalsSerializer
from rest_framework.decorators import api_view
from .models import Hospitals ,HospitalService
from .serializers import HospitalsSerializer,HospitalServecSerializer
from rest_framework import permissions
# Create your views here.


    
class HospitalsList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Hospitals.objects.all()
    serializer_class = HospitalsSerializer
    
class HospitalServesViewList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = HospitalService
    serializer_class = HospitalServecSerializer

@api_view(['GET'])
def getSingleHospitalsData(request, pk):
    hospital = Hospitals.objects.get(ip_h=pk)
    serializer = HospitalsSerializer(hospital, many=False)
    return Response(serializer.data)


class RegisterHospitalAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = HospitalRegisterSerializer
