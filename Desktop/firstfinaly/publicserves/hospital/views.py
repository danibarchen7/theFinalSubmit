from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import *
from rest_framework.decorators import api_view,APIView
from .models import Hospitals ,HospitalService
from rest_framework import permissions
# Create your views here.
from rest_framework import status

    
class HospitalsList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Hospitals.objects.all()
    serializer_class = HospitalsSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SingleHospitalView(APIView):
    def get (self,request,pk):
        hospital = Hospitals.objects.get(ip_h=pk)
        serializer = HospitalsSerializer(hospital, many=False)
        return Response(serializer.data)
    def delete(self,request,pk):
      hospital = Hospitals.objects.get(ip_h=pk)
      hospital.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):

        hospital = Hospitals.objects.get(ip_h=pk)
        serializer = HospitalsSerializer(hospital, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class HospitalServesViewList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = HospitalService
    serializer_class = HospitalServecSerializer



class RegisterHospitalAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = HospitalRegisterSerializer

class ReviewView(APIView):
    serializer_class = ReviewSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
