from django.urls import  path 
from .views import bookings_list
from .views import inventory_list


urlpatterns = [
    path('allbooking', bookings_list),
    path('alitems', inventory_list),
]
