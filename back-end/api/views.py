from telnetlib import STATUS
from .models import Bookings, Inventory
from .serializers import BookingsSerializers,InventorySerializers
from django.http import JsonResponse
from rest_framework.parsers import JSONParser


def inventory_list(request):
    #get all available items
    if request.method == 'GET':
        inventory = Inventory.objects.all()
        serializer =InventorySerializers(inventory, many=True)
        return JsonResponse(serializer.data, safe= False )

def bookings_list(request):
    #get all bookings from the database
    if request.method == 'GET':
        allbookings = Bookings.objects.all()
        serializer =  BookingsSerializers(allbookings, many=True)
        return JsonResponse(serializer.data, safe= False)
    
    elif request.method == 'POST':
        data = JSONParser.objects(request)
        serializer =  BookingsSerializers(data= data)
        if serializer.is_valid():
            serializer.save
            return JsonResponse(serializer.data, status=201)            
        return JsonResponse(serializer.errors, status=400)





