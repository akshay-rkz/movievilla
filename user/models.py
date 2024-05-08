from django.db import models
from adminapp.models import *
# Create your models here.
class Customer(models.Model):
    email=models.CharField(max_length=34)
    username=models.CharField(max_length=34)
    phonenumber=models.IntegerField(null=True)
    password=models.CharField(max_length=34)

class Contact(models.Model):
    userid=models.ForeignKey(Customer,on_delete=models.CASCADE)
    message=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

class Wishlist(models.Model):
    userid=models.ForeignKey(Customer,on_delete=models.CASCADE)
    films=models.ForeignKey(Movies,on_delete=models.CASCADE) 
    date=models.DateField(auto_now_add=True)

class Comments(models.Model):
    userid=models.ForeignKey(Customer,on_delete=models.CASCADE)
    movieid=models.ForeignKey(Movies,on_delete=models.CASCADE,null=True)
    comment=models.TextField()
    time=models.DateField(auto_now_add=True)

class Likes(models.Model):
    userid=models.ForeignKey(Customer,on_delete=models.CASCADE)
    movieid=models.ForeignKey(Movies,on_delete=models.CASCADE)

class DISlikes(models.Model):
    userid=models.ForeignKey(Customer,on_delete=models.CASCADE)
    movieid=models.ForeignKey(Movies,on_delete=models.CASCADE)
