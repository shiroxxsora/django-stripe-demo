import os
from decimal import Decimal

import requests
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.http import JsonResponse

from .models import Item, Order
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
        success_url=f'{base_url}success',
        cancel_url=f'{base_url}cancel',
    )

    return JsonResponse(session)


def success(request):
    return render(request, 'success.html')


def cancel(request):
    return render(request, 'cancel.html')


def index(request):
    base_url = request.build_absolute_uri('/')
    return render(request, 'index.html', {'base_url': base_url})

def order_detail(request, id):
    order = get_object_or_404(Order, id=id)
    items = order.items.all()
    STRIPE_PUBLIC_KEY = settings.STRIPE_PUBLIC_KEY
    return render(request, 'order_detail.html', {'order': order, 'items': items, 'STRIPE_PUBLIC_KEY': STRIPE_PUBLIC_KEY})


def buy_order_detail(request, id):
    order = get_object_or_404(Order, id=id)

    base_url = request.build_absolute_uri('/')

    line_items = []

    for item in order.items.all():
        if item.currency != order.currency:
            conversion_rate = get_conversion_rate(item.currency, order.currency)
            if conversion_rate:
                item_price_converted = Decimal(item.price) * Decimal(conversion_rate)
            else:
                return JsonResponse({'error': 'Unable to fetch conversion rate'}, status=400)
        else:
            item_price_converted = item.price

        line_item = {
            'price_data': {
                'currency': order.currency.lower(),
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': int(item_price_converted) * 100,  # Преобразуем цену в центы
            },
            'quantity': 1,
        }

        if order.tax:
            tax_rate = stripe.TaxRate.create(
                display_name=order.tax.name,
                description=f"{order.tax.name} Tax",
                percentage=float(order.tax.percentage),
                inclusive=False,
                jurisdiction=order.tax.jurisdiction
            )
            line_item['tax_rates'] = [tax_rate.id]

        line_items.append(line_item)

        discounts = []
        if order.discount:
            discounts.append({
                'coupon': order.discount.code
            })

    session = stripe.checkout.Session.create(
        line_items=line_items,
        mode='payment',
        discounts=discounts,
        success_url=f'{base_url}success',
        cancel_url=f'{base_url}cancel',
    )

    return JsonResponse(session)


def get_conversion_rate(from_currency, to_currency):
    api_url = f'https://api.exchangerate-api.com/v4/latest/{from_currency}'
    response = requests.get(api_url)
    data = response.json()

    if 'rates' in data and to_currency in data['rates']:
        return data['rates'][to_currency]
    return None

