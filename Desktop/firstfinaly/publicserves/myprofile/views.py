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
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
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


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


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


class UserViewSet(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        user = MyProfile.objects.get()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
