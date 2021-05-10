from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import aadhar_model
from .serializers import aadhar_modelSerializer
from django.http import JsonResponse


@api_view(['GET', 'POST'])
def homepage(request,number):

    if request.method == 'GET':
        aadhar_data = aadhar_model.objects.filter(aadhar_number=number)
        if aadhar_data:
            serializer = aadhar_modelSerializer(aadhar_data, many=True)
            return JsonResponse(serializer.data,safe=False)
        else:
            voter_data=aadhar_model.objects.filter(voter_id=number)    
            serializer = aadhar_modelSerializer(voter_data, many=True)
            return JsonResponse(serializer.data,safe=False)

    # elif request.method == 'POST':
    #     serializer = SnippetSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)            