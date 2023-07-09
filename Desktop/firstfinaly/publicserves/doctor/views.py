from rest_framework import generics
from rest_framework import permissions, status
from .models import Doctors
from .serializers import *
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
# Create your views here.
from rest_framework.response import Response
# from .forms import AddForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, serializers, status, permissions





class DoctorsList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Doctors.objects.all()
    serializer_class = DoctorSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SingleDoctorView(APIView):
    def get (self,request,pk):
        doctor = Doctors.objects.get(id=pk)
        serializer = DoctorSerializer(doctor, many=False)
        return Response(serializer.data)
    def delete(self,request,pk):
      doctor = Doctors.objects.get(id=pk)
      doctor.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):

        doctor = Doctors.objects.get(id=pk)
        serializer = DoctorSerializer(doctor, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class RegisterDoctorAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = DoctorRegisterSerializer


class ReviewView(APIView):
    serializer_class = ReviewSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
