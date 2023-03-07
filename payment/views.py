import stripe
import json

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

from basket.basket import Basket

# Create your views here.


@login_required
def BasketView(request):
    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace(".", "")
    total = int(total)  # API converts 1899 to 18.99

    stripe.api_key = "sk_test_51MiygNHCokBIog8LOx0fYKaNpONaPRGClNtMwCi92TwV3ZOM5801R5ODAdwb13idufEhZH7OYGiG2lGKmnNRimx500GdTYJ5CQ"
    intent = stripe.PaymentIntent.create(
        amount=total, currency="usd", metadata={"userid": request.user.id}
    )
    return render(request, "payment/home.html", {"client_secret": intent.client_secret})
