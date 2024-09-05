from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Products(models.Model):
    category=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    desc=models.CharField(max_length=1000)
    price=models.IntegerField(default=0)
    image=models.ImageField(default='default.png')
    trending=models.BooleanField(default=0)
    offer=models.BooleanField(default=0)

class Cart(models.Model):
    image=models.ImageField(default='default.png')
    category=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    desc=models.CharField(max_length=1000)
    price=models.IntegerField(default=0)
    quantity=models.IntegerField(default=0)
    totalprice=models.IntegerField(default=0)
    host=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name  #it will return refference name in query set or for get it return name

class Contact(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.CharField(max_length=500)
    host=models.ForeignKey(User,on_delete=models.CASCADE)

class Checkout(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    address=models.TextField(max_length=500)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zipcode=models.IntegerField(null=True)
    country=models.CharField(max_length=100)
    phone=models.IntegerField(null=True)

    payment_method=(("CC","Credit Card"),
                    ("PP","PayPal"),
                    ("COD","Cash on delivery"))
    payment=models.CharField(max_length=100,choices=payment_method)

    comments=models.TextField(max_length=500)
    date=models.DateField(default=datetime.date.today)
    host=models.ForeignKey(User,on_delete=models.CASCADE)