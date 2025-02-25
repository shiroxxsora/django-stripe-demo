import os

from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.http import JsonResponse

from .models import Item
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def item_detail(request, id):
    item = get_object_or_404(Item, id=id)
    STRIPE_PUBLIC_KEY = settings.STRIPE_PUBLIC_KEY
    return render(request, 'item_detail.html', {'item': item, 'STRIPE_PUBLIC_KEY': STRIPE_PUBLIC_KEY})


def buy_detail(request, id):
    item = get_object_or_404(Item, id=id)

    base_url = request.build_absolute_uri('/')

    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': f'{ item.currency.lower() }',
                'product_data': {
                    'name': f'{ item.name }',
                },
                'unit_amount': f'{ int(item.price) * 100 }',
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=f'{base_url}/success',
        cancel_url=f'{base_url}/cancel',
    )

    return JsonResponse(session)

def success(request):
    return render(request, 'success.html')

def cancel(request):
    return render(request, 'cancel.html')