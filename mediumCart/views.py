from django.shortcuts import render


def about(request):
    return render(request, "about/index.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("fullName")
        email = request.POST.get("email")
        issue = request.POST.get("issue")
        # Now insert them into the database "contact.sqlite3"
    return render(request, "contact/index.html")
