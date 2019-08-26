from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .paytm import checksum
import hashlib
import time


class EndPoint:
    def __init__(self):
        pass

    @staticmethod
    def index(request, productId):
        paytmParams = {
            "MID": "WorldP64425807474247",
            "ORDER_ID": hashlib.sha1(
                str(productId).encode("utf-8") + str(time.time()).encode("utf-8")
            ).hexdigest()[-15:],
            "TXN_AMOUNT": "3000",
            "CUST_ID": "acfff@paytm.com",
            "INDUSTRY_TYPE_ID": "Retail",
            "WEBSITE": "WEBSTAGING",
            "CHANNEL_ID": "WEB",
            "CALLBACK_URL": "http://127.0.0.1:8000/payment/pay/",
        }
        print(paytmParams["ORDER_ID"])
        paytmParams["CHECKSUMHASH"] = checksum.generate_checksum(
            paytmParams, "kbzk1DSbJiV_O3p5"
        )
        return render(request, "payment/index.html", paytmParams)

    @csrf_exempt
    def payRequest(request):
        # Paytm will send post request here.
        form = request.POST
        responseDict = {}
        for i in form.keys():
            responseDict[i] = form[i]
            if i == "CHECKSUMHASH":
                Checksum = form[i]
        print(responseDict)
        verify = checksum.verify_checksum(responseDict, "kbzk1DSbJiV_O3p5", Checksum)
        if verify:
            if responseDict["RESPCODE"] == "01":
                print("order-success")
                return render(request, "checkout/thankYou.html")
            else:
                print("order-unsuccess")
                return render(request, "checkout/failed.html")
