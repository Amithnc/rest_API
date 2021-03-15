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
def homepage(request,aadhar_number):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        print(aadhar_number)
        aadhar_data = aadhar_model.objects.filter(aadhar_number=aadhar_number)
        serializer = aadhar_modelSerializer(aadhar_data, many=True)
        return JsonResponse(serializer.data,safe=False)

    # elif request.method == 'POST':
    #     serializer = SnippetSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)            