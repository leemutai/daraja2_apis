from django.shortcuts import render


# Create your views here.
def initiate_payment(request):
    if request.method == "POST":
        phone = request.POST["phone"]
        amount = request.POST["amount"]
        print(phone, amount)
    return render(request, "payment.html")


def callback(request):
    return None
