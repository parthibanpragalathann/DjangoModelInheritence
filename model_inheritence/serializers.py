from .models import Customer, Staff, Place, Restaurants, Person, Employ
from rest_framework import serializers

class Customer_serilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ("id", "url", "name", "email", "address", "phone")


class Staff_serilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Staff
        fields = ("id", "url", "name", "email", "address", "position")


class Place_serilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = ("id", "url", "name", "address")


class Restaurants_serilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurants
        fields = ("id", "url", "name", "address", "serves_pizza", "serves_pasta")

class Person_serilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ("id", "url", "first_name", "last_name")

class Employ_serilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employ
        fields = ("id", "url", "first_name", "last_name")
