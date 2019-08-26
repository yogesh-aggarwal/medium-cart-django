from django.urls import path
from . import views

urlpatterns = [
    path("<int:productId>", views.EndPoint.index, name="Payment"),
    path("pay/", views.EndPoint.payRequest, name="Payment"),
]
