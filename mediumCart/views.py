from django.shortcuts import render
from django.http import HttpResponse


def about(request):
    return render(request, "about/index.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("fullName")
        email = request.POST.get("email")
        issue = request.POST.get("issue")
        # Now insert them into the database "contact.sqlite3"
    return render(request, "contact/index.html")

def thankYou(request):
    if request.method == "POST":
        # Generate hash id here
        attributes ={
            "id": "someHash"
        }
        return render(request, "checkout/thankYou.html", attributes)
    else:
        return HttpResponse('<h1 style="font-family: Verdana, Geneva, Tahoma, sans-serif">500 Internel server error!</h1>')
