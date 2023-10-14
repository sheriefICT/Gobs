from django.shortcuts import render
from django.http.response import  JsonResponse 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import * 
from .serializers import *



#1- without Rest Framework and  model query 
# def no_rest_from_model_query(request):
#     data = Guest.objects.all()
#     response = {
#         'guests': list(data.values('name','mobile')) 
#     }
#     return JsonResponse(response)



#2 function based on views
@api_view(['GET', 'POST'])
def rest_for_function_based_views_List(request):      
    #GET
        if request.method == 'GET':
            guests = Guest.objects.all()
            serializers = GuestSerializer(guests, many=True)
            return Response(serializers.data)      
    #POST
        elif request.method == 'POST':
            serializer = GuestSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= status.HTTP_201_CREATED)
            return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
              


@api_view(['GET', 'POST', 'DELETE'])
def rest_for_function_based_views_List_as_pk(request, pk):
        try:
            guests = Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
             return Response(status= status.HTTP_404_NOT_FOUND)    
     #GET
        if request.method == 'GET':
            serializers = GuestSerializer(guests)
            return Response(serializers.data)      
    #PUT
        elif request.method == 'PUT':
            serializer = GuestSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    #DELETE
        if request.method == 'DELETE':
            guests.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)      

# class based views

