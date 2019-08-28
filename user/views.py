from django.shortcuts import render


class EndPoint:
    def __init__(self):
        pass

    @staticmethod
    def index(request):
        return render(request, "user/index.html")

    @staticmethod
    def security(request):
        return render(request, "user/security.html")

    @staticmethod
    def address(request):
        return render(request, "user/address.html")

    @staticmethod
    def payment(request):
        return render(request, "user/payment.html")

    @staticmethod
    def stuff(request):
        return render(request, "user/stuff.html")
