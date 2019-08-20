from django.shortcuts import render
from sql_tools import sqlite

class EndPoint:
    def __init__(self):
        pass
    
    @staticmethod
    def index(request):
        attributes = {
            "title": "Medium cart",
            "products": Tools.parseData(Tools.fetchDatabase())
        }
        return render(request, "home/index.html", attributes)

class Tools:
    def __init__(self):
        pass
    
    @staticmethod
    def fetchDatabase(kind="Product"):
        sqlite.constants.__databPath__ = []
        sqlite.connect("database/data/products.sqlite3")
        return sqlite.execute(f"SELECT * FROM {kind.upper()}")

    @staticmethod    
    def parseData(data):
        data = data[0]
        parse = {}
        for record in data:
            parse[record[0]] = {
                "endId": record[1],
                "name": record[2],
                "shortDesc": record[3],
                "description": record[4],
                "images": record[5].split(" =+=+=@#$%^&*()=+=+= "),
                "rating": record[6],
                "owners": record[7].split(" =+=+=@#$%^&*()=+=+= "),
                "categories": record[8].split(" =+=+=@#$%^&*()=+=+= "),
                "reviews": record[9].split(" =+=+=@#$%^&*()=+=+= "),
                "assets": record[10].split(" =+=+=@#$%^&*()=+=+= "),
                "quantity": record[11].split(" =+=+=@#$%^&*()=+=+= "),
                "sale": record[12],
            }
        print(parse["125785"]["reviews"])
        return parse
