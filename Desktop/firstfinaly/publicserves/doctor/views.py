from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from rest_framework import generics
from rest_framework import permissions, status
from .models import Doctors
from .serializers import DoctorRegisterSerializer, DoctorSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.generic.edit import CreateView
from rest_framework.serializers import ModelSerializer
# from .forms import AddForm
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, serializers, status, permissions
# from rest_framework.authentication import TokenAuthentication
# from django.contrib.auth import authenticate, login, logout
# from django.shortcuts import render, redirect


# # class DoctorLoginView(APIView):
#     permission_classes = (permissions.AllowAny,)
#     authentication_classes = (TokenAuthentication,)

#     def post(self, request):
#         fullname = request.data.get('fullname')
#         password = request.data.get('password')

#         user = authenticate(fullname=fullname, password=password)
#         if user is not None:
#             token = Token.objects.create(user=user)
#             login(request, user)
#             # login(request, user)
#             request.META['HTTP_AUTHORIZATION'] = 'Token ' + token.key
#             return Response("login done")
#             # return Response({"token": token.key})
#         else:
#             return Response({'error': 'Invalid credentials'})


class DoctorProfileView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        user = request.user
        return Response({'fullname': user.fullname, 'email': user.email, 'phone': user.phone})


class DoctorLogoutView(APIView):
    def post(self, request):
        user = request.user
        token = Token.objects.get(user=user)
        token.delete()
        return Response({'message': 'Logout successful'})


# class AddDoctorView(CreateView):
#     form_class = AddForm
#     tamplate_name = 'add.html'
#     success_url = '/doctors/'

# dealing with doctors


# def update_view(request, id):
#     # dictionary for initial data with
#     # field names as keys
#     context = {}

#     # fetch the object related to passed id
#     obj = get_object_or_404(Doctors, id=id)

#     # pass the object as instance in form
#     form = AddForm(request.POST or None, instance=obj)

#     # save the data from the form and
#     # redirect to detail_view
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect("/"+id)

#     # add form dictionary to context
#     context["form"] = form

#     return render(request, "update_view.html", context)
# @api_view(['GET'])
# def getDoctorsData(request):
#     doctors = Doctors.objects.all()
#     serializer = DoctorSerializer(doctors, many=False)
#     return Response(serializer.data)


@api_view(['GET'])
def getSingleDoctorData(request, pk):
    doctor = Doctors.objects.get(id=pk)
    serializer = DoctorSerializer(doctor, many=False)
    return Response(serializer.data)


class DoctorsList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Doctors.objects.all()
    serializer_class = DoctorSerializer


# class DoctorDetail(generics.ListCreateAPIView):
#     queryset = Doctors.objects.all()
#     serializer_class = DoctorSerializer

# class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [permissions.AllowAny]
#     queryset = Doctors.objects.all()
#     serializer_class = DoctorSerializer


class RegisterDoctorAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = DoctorRegisterSerializer
