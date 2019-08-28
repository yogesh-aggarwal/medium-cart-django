"""mediumCart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls"), name="Home"),
    path("blog/", include("blog.urls"), name="Blog"),
    path("checkout/", include("checkout.urls"), name="Checkout"),
    path("user/", include("user.urls"), name="User"),
    path("about/", views.about, name="About"),
    path("cart/", include("cart.urls"), name="Cart"),
    path("contact/", views.contact, name="Contact"),
    path("view/", include("view.urls"), name="View"),
    path("payment/", include("payment.urls"), name="Payment"),
    path("thank-you/", views.thankYou, name="Thank-you"),
    path("fail", views.fail, name="Failed-payment"),
]

handler404 = 'mediumCart.views.handler404'
