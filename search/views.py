from django.shortcuts import render
from sql_tools import sqlite


class EndPoint:
    def __init__(self):
        pass

    @staticmethod
    def index(request, query):
        sqlite.connect(
            "/media/yogesh/Development/Python/django/mediumCart/database/data/products.sqlite3",
            raiseError=False,
        )

        # Perform search functionality here

        result = []

        attributes = {
            "query": query,
            "result": result
        }
        return render(request, "search/index.html", attributes)