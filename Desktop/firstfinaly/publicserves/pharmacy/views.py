from django.shortcuts import render

# Create your views here.
from .models import Pharmacies
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from myprofile.models import MyProfile
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework.response import Response
from django.views.generic import ListView, DetailView
from rest_framework import viewsets
from pharmacy.models import *
from pharmacy.serializers import PharmacySerializer, UserSerializer, PharmacyRegisterSerializer
from rest_framework import mixins
from rest_framework import permissions
# from .permissions import IsOwnerOrReadOnly


# filtering the data about the medicn
from django.db.models import Q


def is_valid_queryparam(param):
    return param != '' and param is not None


def filter(request):
    qs = Pharmacies.objects.all()
    name = request.GET.get("the name of input in the html")
# for each input filter we will do the same thing to it
    if is_valid_queryparam(name):
        # here we pass to the filter the filled that we want
        # to do filtering on it and __icontains it to make check
        # and the __i its mean that the filed is a case sensative
        qs = qs.filter(name__icontains=name)

    context = {
        'queryset': qs
    }
    return render(request, "the react page", context)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'pharmacies': reverse('PharmaciesList', request=request, format=format)
    })


@api_view(['GET', 'POST'])
def getPharmacyData(request):
    pharmacy = Pharmacies.objects.all()
    serializer = PharmacySerializer(pharmacy, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getSinglePharmacy(request, pk):
    pharmacy = Pharmacies.objects.get(id=pk)
    serializer = PharmacySerializer(pharmacy, many=False)
    return Response(serializer.data)


class RegisterPharmacyAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PharmacyRegisterSerializer
