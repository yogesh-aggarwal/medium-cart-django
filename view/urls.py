from django.urls import path, include
from . import views

urlpatterns = [
    # path("", include("home.urls"), name="Home"),
    path("<int:productId>", views.EndPoint.index, name="Product view"),
]
