# from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Web3event
from .serializers import Web3eventSerializer

@api_view(['GET', 'POST'])
def event_list(request):
    """
    Lis all web3 events or create a new event
    """
    if request.method == 'GET':
        events = Web3event.objects.all()
        serializer = Web3eventSerializer(events, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = Web3eventSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status = status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def event_detail(request, pk):
    """
    Retrieve, update or delete a event
    """
    try:
        event = Web3event.objects.get(pk = pk)
    except Web3event.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = Web3eventSerializer(event)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = Web3eventSerializer(event, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status = status.HTTP_200_OK)
        return Response(serializer.errors,
                        status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        serializer = Web3eventSerializer(event)
        serializer.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

