from django.http import JsonResponse
from .models import Gear
from .serializers import GearSerializer 
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status

@api_view(['GET', 'POST'])
def gear_list(request, format=None):

    if request.method == 'GET':
        gear = Gear.objects.all()
        serializer = GearSerializer(gear, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = GearSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
          
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def gear_detail(request, id, format=None):
    try:
        gear = Gear.objects.get(pk=id)
    except Gear.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GearSerializer(gear)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = GearSerializer(gear, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        gear.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 