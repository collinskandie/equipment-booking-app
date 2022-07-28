from sqlite3 import Date, Timestamp
from django.db import models

class SystemUsers(models.Model):
    personalNo = models.CharField(max_length=100,primary_key=True)
    username= models.CharField(max_length=100)
    department= models.CharField(max_length=120)
    userType = models.CharField(max_length=100)
    phoneNumber= models.IntegerField()
    emailAddress = models.EmailField()
    user_password= models.CharField(max_length=128)
    date_created=models.DateTimeField()
    last_login = models.DateTimeField()
    def __str__(self):
        return self.personalNumber
class Inventory(models.Model):
    description = models.CharField(max_length=100)
    status= models.CharField(max_length=100)
    other_info = models.TextField()

    def __str__(self):
        return self.description

class Bookings(models.Model):
    item_id= models.CharField(max_length=100)
    accessories= models.TextField()
    user_id= models.CharField(max_length=100)
    date= models.DateTimeField()
    timefrom= models.TimeField()
    timeto= models.TimeField()
    bookingdate= models.DateTimeField()
    honApprovalStatus= models.CharField(max_length=100)
    honApprovalTime=models.DateTimeField()
    honId=models.CharField(max_length=100)
    honComments = models.TextField()
    ctvpApprovalStatus= models.CharField(max_length=100)
    ctvpApprovalTime=models.DateTimeField()
    ctvpId=models.CharField(max_length=100) 
    ctvComments =models.TextField()
    cstoApprovalStatus= models.CharField(max_length=100)
    cstoApprovalTime=models.DateTimeField()
    cstoId=models.CharField(max_length=100) 
    ctvComments =models.TextField() 

    def __str__(self):
        return self.id