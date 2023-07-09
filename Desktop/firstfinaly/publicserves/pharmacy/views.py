
from rest_framework import status
# Create your views here.
from .models import Pharmacies
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework.response import Response
from pharmacy.models import *
from pharmacy.serializers import *

# from .permissions import IsOwnerOrReadOnly


# filtering the data about the medicn

class PharmacyListView(APIView):
    permission_classes = (AllowAny,)
    queryset = Pharmacies.objects.all()
    serializer_class  = PharmacySerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ReviewView(APIView):
    serializer_class = ReviewSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SinglePharmacy(APIView):
    def get (self,request,pk):
        pharmacy = Pharmacies.objects.get(id=pk)
        serializer = PharmacySerializer(pharmacy, many=False)
        return Response(serializer.data)
    def delete(self,request,pk):
      pharmacy = PharmacySerializer.objects.get(id=pk)
      pharmacy.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):

        pharmacy = Pharmacies.objects.get(id=pk)
        serializer = PharmacySerializer(pharmacy, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class MedicenList(APIView):
    permission_classes= (AllowAny,)
    queryset = Medicines.objects.all()
    serializer_class = MedicenSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class SingleMedicenView(APIView):
    def get (self,request,pk):
        medicen = Medicines.objects.get(ip_m=pk)
        serializer = MedicenSerializer(medicen, many=False)
        return Response(serializer.data)
    def delete(self,request,pk):
      medicen = Medicines.objects.get(ip_m=pk)
      medicen.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):

        medicen = Medicines.objects.get(ip_m=pk)
        serializer = MedicenSerializer(medicen, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class RegisterPharmacyAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PharmacyRegisterSerializer
