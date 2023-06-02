from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from pharmacy.models import Pharmacies
from doctor.models import Doctors
from .serializers import PharmacySerializer, DoctorsSerializer
# Create your views here.


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/pharmacy/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of doctors'
        },
        {
            'Endpoint': '/pharmacy/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single doctor object'
        },
        {
            'Endpoint': '/transport/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/transport/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/transport/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)


@api_view(['GET'])
def getData(request):
    pharmacy = Pharmacies.objects.all()
    serializer = PharmacySerializer(pharmacy, many=True)
    return Response(serializer.data)

# to process one object from the database


@api_view(['GET'])
def getSingleData(request, pk):
    pharmacy = Pharmacies.objects.get(ip_ph=pk)
    serializer = PharmacySerializer(pharmacy, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getDoctorsDate(request, pk):
    doctors = Doctors.objects.all()
    serializer = DoctorsSerializer(doctors, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getSingleDoctorData(request, pk):
    doctor = Pharmacies.objects.get(ip_ph=pk)
    serializer = DoctorsSerializer(doctor, many=False)
    return Response(serializer.data)
