from django.urls import path
from . import views

urlpatterns = [
    path("", views.EndPoint.index, name="Payment"),
]
