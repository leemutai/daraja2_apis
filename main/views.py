import logging

from django.shortcuts import render

logger = logging.getLogger(__name__)
# Create your views here.
def initiate_payment(request):
    if request.method == "POST":
        phone = request.POST["phone"]
        amount = request.POST["amount"]
        logger.info(f"{phone} {amount}")

    return render(request, "payment.html")


def callback(request):
    return None
