from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view
from rest_framework import generics, serializers, status, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from .serializers import MyProfileSerializer, RegisterSerializer, LoginSerializer
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import MyProfile

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User
import jwt
from django.conf import settings
# from .serializers import PhonePasswordSerializer
from rest_framework.authtoken.models import Token


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (TokenAuthentication,)

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            token = Token.objects.create(user=user)
            login(request, user)
            # login(request, user)
            request.META['HTTP_AUTHORIZATION'] = 'Token ' + token.key
            return redirect('myprofile:profile')
            # return Response({"token": token.key})
        else:
            return Response({'error': 'Invalid credentials'})


class ProfileView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        user = request.user
        return Response({'username': user.username, 'email': user.email, 'phone': user.phone})


class LogoutView(APIView):
    def post(self, request):
        user = request.user
        token = Token.objects.get(user=user)
        token.delete()
        return Response({'message': 'Logout successful'})




class LoginAPIView(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone = request.data['phone']
        password = request.data['password']

        user = authenticate(phone=phone, password=password)

        if user is not None and user.is_active:
            token, created = Token._default_manager.get_or_create(user=user)
            return Response({
                'token': token.key,
                'created': created
            })
        else:
            return Response({'error': 'Invalid phone number or password'})


class MyProfileView(APIView):

    def get(self, reques,pk):
        user = MyProfile.objects.get(id=pk)
        serializer = MyProfileSerializer(user)
        return Response(serializer.data)
    def delete(self,request,pk):
      user = MyProfile.objects.get(id=pk)
      user.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):

        user = MyProfile.objects.get(id=pk)
        serializer = MyProfileSerializer(user, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    

@api_view(['GET'])   
def  getRoutes(request):
    routes = [
        {
            'Endpoint': '/myprofile',
            'method': 'GET',
            'body':None,
            'description': 'Return the user info'
        },
        {
            'Endpoint': '/pharmacy',
            'method': 'GET',
            'body':None,
            'description': 'Return the pharmcy info and list all the pharmacies'
        }
        ,
        {
            'Endpoint': '/doctors',
            'method': 'GET',
            'body':None,
            'description': 'Return the doctors info and list all the doctors'
        }
        ,
        {
            'Endpoint': '/hospitals',
            'method': 'GET',
            'body':None,
            'description': 'Return the hospital info and list all the hospitals'
        }
        ,
        {
            'Endpoint': '/mechanicals',
            'method': 'GET',
            'body':None,
            'description': 'Return the mechanical info and list all the mechanicals'
        },
        {
            'Endpoint': '/trasportcom',
            'method': 'GET',
            'body':None,
            'description': 'Return the trasportcompany info and list all the trasportcompanies'
        }
    ]
    return Response({'routes':routes})
