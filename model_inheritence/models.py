'''
Abstract base classes: Use this when the parent class contains common fields and the parent class
table is not desirable.Multi-table inheritance: Use this when the parent class has common fields,
but the parent class table also exists in the database all by itself.Proxy models: Use this when 
you want to modify the behavior of the parent class, like by changing orderby or a new model manager.
'''

# Create your models here.
from django.db import models


class ContactInfo(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    address = models.TextField(max_length=20)

    class Meta:
        abstract = True


class Customer(ContactInfo):
    phone = models.IntegerField()


class Staff(ContactInfo):
    position = models.CharField(max_length=10)


class Place(models.Model):
    name = models.CharField(max_length=20)
    address = models.TextField(max_length=20)

    def __str__(self):
        return self.name


class Restaurants(Place):
    serves_pizza = models.BooleanField(default=False)
    serves_pasta = models.BooleanField(default=False)

    def __str__(self):
        return self.serves_pasta


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Employ(Person):
    class Meta:
        proxy = True

    def fullName(self):
        return self.first_name + " " + self.last_name