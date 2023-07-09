from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
# Create your views here.
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework import status
# dealing with doctors




class SingleMechanicalView(APIView):
    def get (self,request,pk):
        mechanical = Mechanical.objects.get(ip_m=pk)
        serializer = MechanicalSerializer(mechanical, many=False)
        return Response(serializer.data)
    def delete(self,request,pk):
      mechanical = Mechanical.objects.get(ip_m=pk)
      mechanical.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):

        mechanical = Mechanical.objects.get(ip_m=pk)
        serializer = MechanicalSerializer(mechanical, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class MechanicalsList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Mechanical.objects.all()
    serializer_class = MechanicalSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class TypeVechaleList(APIView):
    permission_classes = [permissions.AllowAny]
    queryset = TypeVechale.objects.all()
    serializer_class = TypeVichaleSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SingleTypeVechaleView(APIView):
    def get (self,request,pk):
        typevi = TypeVechale.objects.get(ip_type=pk)
        serializer = TypeVichaleSerializer(typevi, many=False)
        return Response(serializer.data)
    def delete(self,request,pk):
      typevi = TypeVechale.objects.get(ip_type=pk)
      typevi.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):

        typevi = TypeVechale.objects.get(ip_type=pk)
        serializer = TypeVichaleSerializer(typevi, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


        
class ReviewView(APIView):
    serializer_class = ReviewSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RegisterMechanicalAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = MechanicalRegisterSerializer
