from django.contrib import admin
from django.urls import path
from api.views import bookings_list
from api.views import inventory_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('activebookings/',bookings_list),
    path('activeinventory/',inventory_list)

]
