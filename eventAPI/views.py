# from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Web3event
from .serializers import Web3eventSerializer
from django.http import HttpResponse
from django.core import serializers
import json

def get_all_events(request):
    """
    Lis all web3 events or create a new event
    """

    if request.method == 'GET':
        events = Web3event.objects.all()
        serializers = Web3eventSerializer(events, many = True)

        return HttpResponse("Hello, world!")
    else:
        return HttpResponse("get all error")
    
def create_event(request):

    if request.method == 'POST':
        title = request.POST.get('title')
        summary = request.POST.get('summary')
        
        Web3event.objects.create(title = title, image='', source_url='', event_url='', summary = summary, description='', )
        print("fwefwefwefwefefwewf")
        return HttpResponse("create successfully")
    else :
        return HttpResponse("create error")

        # Web3event.objects.create(title='hello', image='')

        # serializer = Web3eventSerializer(data = request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data,
        #                     status = status.HTTP_201_CREATED)
        # return Response(serializer.errors,
        #                 status = status.HTTP_400_BAD_REQUEST)
    



