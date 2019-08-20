from django.shortcuts import render

class EndPoint:
    def __init__(self):
        pass
    
    @staticmethod
    def index(request):
        attributes = {
            "title": "Medium cart",
            "product": {
                "title": "Apple",
                "shortDesc": "Other than that, it’s an iPhone 8. You’ll get the exact same features and components as in other iPhone 8 models. The iPhone 8 is also available in gold, silver and (“space”) gray. Alas, there’s still no rose gold option",
            }
        }
        return render(request, "home/index.html", attributes)
