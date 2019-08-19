from django.shortcuts import render

class EndPoint:
    def __init__(self):
        pass
    
    @staticmethod
    def index(request):
        attributes = {
            "title": "Medium cart"
        }
        return render(request, "home/index.html", attributes)
