from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    address =  models.CharField(max_length=200)

class Storage(models.Model):
    brand = models.CharField(max_length=100)
    model =  models.CharField(max_length=100)
    quantity =  models.IntegerField()

class Product(models.Model):
    storage = models.ForeignKey(Storage)
    serial_number = models.CharField(max_length=100)

#class Choice(models.Model):
#    poll = models.ForeignKey(Poll)
#    choice = models.CharField(max_length=200)
#    votes = models.IntegerField()

