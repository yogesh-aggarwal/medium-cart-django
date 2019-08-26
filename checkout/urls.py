from django.urls import path
from . import views

urlpatterns = [
    path("<int:productId>", views.EndPoint.index, name="Checkout"),
]
