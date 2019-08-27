from django.shortcuts import render
from django.http import HttpResponse
from sql_tools import sqlite


def about(request):
    return render(request, "about/index.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("fullName")
        email = request.POST.get("email")
        issue = request.POST.get("issue")
        print(name, email, issue)
        sqlite.connect("contacts.sqlite3", validateDatabase=False, raiseError=False)
        # INSERT DATA INTO DATABASE
    return render(request, "contact/index.html")

def thankYou(request):
    if request.method == "POST":
        return render(request, "checkout/thankYou.html")
    else:
        return HttpResponse('<h1 style="font-family: Verdana, Geneva, Tahoma, sans-serif">500 Internel server error!</h1>')

def fail(request):
    if request.method == "GET":
        return render(request, "checkout/failed.html")
    else:
        return HttpResponse('<h1 style="font-family: Verdana, Geneva, Tahoma, sans-serif">500 Internel server error!</h1>')
