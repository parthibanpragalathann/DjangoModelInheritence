from .models import Customer, Staff, Place, Restaurants, Person, Employ
from .serializers import Customer_serilizer, Staff_serilizer, Place_serilizer, Restaurants_serilizer, Person_serilizer, Employ_serilizer
from rest_framework import viewsets

# Create athletics views here.
class CustomerDetail(viewsets.ModelViewSet):
    queryset = Customer.objects.order_by("name")
    serializer_class = Customer_serilizer

class StaffDetail(viewsets.ModelViewSet):
    queryset = Staff.objects.order_by("name")
    serializer_class = Staff_serilizer

class PlaceDetail(viewsets.ModelViewSet):
    queryset = Place.objects.order_by("name")
    serializer_class = Place_serilizer

class RestaurantsDetail(viewsets.ModelViewSet):
    queryset = Restaurants.objects.order_by("name")
    serializer_class = Restaurants_serilizer

class PersonDetails(viewsets.ModelViewSet):
    queryset = Person.objects.order_by("first_name")
    serializer_class = Person_serilizer

class EmployDetails(viewsets.ModelViewSet):
    queryset = Employ.objects.order_by("first_name")
    serializer_class = Employ_serilizer