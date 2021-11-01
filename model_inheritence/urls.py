from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register("customer", views.CustomerDetail)
router.register("staff", views.StaffDetail)
router.register("place", views.PlaceDetail)
router.register("rest", views.RestaurantsDetail)
router.register("person", views.PersonDetails)
router.register("employ", views.EmployDetails)

urlpatterns = [
    path("", include(router.urls))
]