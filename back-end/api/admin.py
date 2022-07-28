from django.contrib import admin
from .models import SystemUsers
from .models import Inventory
from .models import Bookings

#admin.site.register(SystemUsers)
@admin.register(SystemUsers)
class UserModel(admin.ModelAdmin): 
    list_filter =()
@admin.register(Inventory)
class InventoryModel(admin.ModelAdmin): 
    list_filter =()
@admin.register(Bookings)
class BookingsModel(admin.ModelAdmin): 
    list_filter =()