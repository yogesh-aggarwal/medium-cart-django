from django.shortcuts import render
from django.http import HttpResponseRedirect
from sql_tools import sqlite


class EndPoint:
    def __init__(self):
        pass

    @staticmethod
    def index(request):
        query = request.GET.get("query")
        print(query)

        sqlite.connect(
            "/media/yogesh/Development/Python/django/mediumCart/database/data/products.sqlite3",
            raiseError=False,
        )

        result = []
        # Perform search functionality here

        attributes = {"query": query, "result": result}
        if query is not "":
            return render(request, "search/index.html", attributes)
        else:
            return HttpResponseRedirect("/")
