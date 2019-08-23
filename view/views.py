from django.shortcuts import render
from sql_tools import sqlite

class EndPoint:
    def __init__(self):
        pass
    
    @staticmethod
    def index(request, productId):
        attributes = {
            "title": "Medium cart",
            "products": Product().parseData(Product.fetchDatabase(productId, "Product"))[f"{productId}"],
            "productId": productId,
        }
        return render(request, "view/index.html", attributes)

class Product:
    def __init__(self):
        pass
    
    @staticmethod
    def fetchDatabase(productId, kind="Product"):
        sqlite.constants.__databPath__ = []
        sqlite.connect("database/data/products.sqlite3")
        return sqlite.execute(f"SELECT * FROM {kind.upper()} WHERE id={productId}",)

    def parseData(self, data):
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
                "quantity": record[11],
                "sale": record[12],
                "price": self.numberSystem(record[13], target="indian")
            }
        return parse

    # @staticmethod
    def numberSystem(self, number, target="indian"):
        if target == "indian":
            intNum = str(number).split(".")[0]
            intLst = list(intNum)

            if len(intNum) == 4:
                intLst.insert(1, ",")
            elif len(intNum) == 5:
                intLst.insert(2, ",")
            elif len(intNum) == 6:
                intLst.insert(1, ",")
                intLst.insert(4, ",")
            elif len(intNum) == 7:
                intLst.insert(2, ",")
                intLst.insert(5, ",")
            elif len(intNum) == 8:
                intLst.insert(1, ",")
                intLst.insert(4, ",")
                intLst.insert(7, ",")
            else:
                return "Overflow"

            try:
                if str(number).split(".")[1] != "0" or str(number).split(".")[1] == "":
                    intNum = f'{"".join(intLst)}.{str(number).split(".")[1]}'
                else:
                    intNum = f'{"".join(intLst)}'
            except Exception:
                intNum = f'{"".join(intLst)}'

            return intNum
