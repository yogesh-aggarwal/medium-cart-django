from django.shortcuts import render

class EndPoint:
    def __init__(self):
        pass
    
    @staticmethod
    def index(request, productId):
        attributes = {
            "productId": None
        }
        if request.method == "POST":
            firstName = request.POST.get("firstName")
            lastName = request.POST.get("lastName")
            address = request.POST.get("address")
            phone = request.POST.get("phone")
            city = request.POST.get("city")
            country = request.POST.get("country")
            state = request.POST.get("state")
            zipCode = request.POST.get("zipCode")
            print(firstName, lastName,address, phone, city, country, state, zipCode)
        if request.method == "GET":
            attributes["productId"] = productId

        return render(request, "checkout/index.html", attributes)
