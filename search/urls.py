from django.urls import path
from . import views

urlpatterns = [
    path("<str:query>", views.EndPoint.index, name="Search"),
]
