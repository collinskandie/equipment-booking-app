from dataclasses import fields
from rest_framework import serializers
from .models import Bookings, Inventory



class BookingsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = ['id','item_id','accessories','user_id','date','timefrom','timeTo','bookingdate']   

class InventorySerializers(serializers.ModelSerializer):
    class Meta:
        Model = Inventory
        fields = ['id', 'description', 'status','other_info']         
       