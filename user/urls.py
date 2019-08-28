from django.urls import path
from . import views

urlpatterns = [
    path("", views.EndPoint.index, name="User"),
    path("/security", views.EndPoint.security, name="Login & Security"),
    path("/address", views.EndPoint.address, name="Address"),
    path("/payment", views.EndPoint.payment, name="Payment"),
    path("/stuff", views.EndPoint.stuff, name="Stuff"),
]
