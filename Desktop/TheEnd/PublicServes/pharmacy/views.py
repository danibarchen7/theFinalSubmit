# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import Pharmacies
# from .serializers import PharmacySerializer
# # Create your views here.


# @api_view(['GET'])
# def getRoutes(request):
#     routes = [
#         {
#             'Endpoint': '/transport/',
#             'method': 'GET',
#             'body': None,
#             'description': 'Returns an array of notes'
#         },
#         {
#             'Endpoint': '/transport/id',
#             'method': 'GET',
#             'body': None,
#             'description': 'Returns a single note object'
#         },
#         {
#             'Endpoint': '/transport/create/',
#             'method': 'POST',
#             'body': {'body': ""},
#             'description': 'Creates new note with data sent in post request'
#         },
#         {
#             'Endpoint': '/transport/id/update/',
#             'method': 'PUT',
#             'body': {'body': ""},
#             'description': 'Creates an existing note with data sent in post request'
#         },
#         {
#             'Endpoint': '/transport/id/delete/',
#             'method': 'DELETE',
#             'body': None,
#             'description': 'Deletes and exiting note'
#         },
#     ]
#     return Response(routes)


# @api_view(['GET'])
# def getData(request):
#     pharmacy = Pharmacies.objects.all()
#     serializer = PharmacySerializer(pharmacy, many=True)
#     return Response(serializer.data)

# # to process one object from the database


# @api_view(['GET'])
# def getSingleData(request, pk):
#     pharmacy = Pharmacies.objects.get(id=pk)
#     serializer = PharmacySerializer(pharmacy, many=False)
#     return Response(serializer.data)
