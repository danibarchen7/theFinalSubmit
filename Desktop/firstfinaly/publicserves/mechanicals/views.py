from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from .models import Mechanical, TypeWork
from .serializers import MechanicalSerializer, MechanicalRegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
# Create your views here.
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework import status
# dealing with doctors


# @api_view(['GET'])
# def getDoctorsData(request):
#     doctors = Doctors.objects.all()
#     serializer = DoctorSerializer(doctors, many=False)
#     return Response(serializer.data)


@api_view(['GET'])
def getSingleMechanaicalData(request, pk):
    mechanical = Mechanical.objects.get(ip_m=pk)
    serializer = MechanicalSerializer(mechanical, many=False)
    return Response(serializer.data)


class MechanicalsList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Mechanical.objects.all()
    serializer_class = MechanicalSerializer


# class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [permissions.AllowAny]
#     queryset = Doctors.objects.all()
#     serializer_class = DoctorSerializer


class RegisterMechanicalAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = MechanicalRegisterSerializer
# class RegisterMechanicalAPIView(APIView):
    # def get(self, request, format=None):
    #     mechanical = Mechanical.objects.all()
    #     serializer = MechanicalSerializer(mechanical, many=True)
    #     return Response(serializer.data)

    # def post(self, request, format=None):

    #     mechanicalserializer = MechanicalSerializer(data=request.data)
    #     typeworkserializer = TypeWorkSerializer(data=request.data)
    #     if mechanicalserializer.is_valid():
    #         mechanicalserializer.save()
    #         return Response(mechanicalserializer.data, status=status.HTTP_201_CREATED)
    #     return Response(typeworkserializer.errors, status=status.HTTP_400_BAD_REQUEST)
