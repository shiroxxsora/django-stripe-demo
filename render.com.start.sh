#!/bin/bash

echo "Running migrations..."
python stripe_demo/manage.py migrate --noinput

echo "Creating superuser..."
python stripe_demo/manage.py createsuperuser --noinput --username root --email admin@example.com

python stripe_demo/manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
user = User.objects.get(username='root')
user.set_password('password123')
user.save()

from payments.models import Item
item1 = Item.objects.create(
     name="Example Item 1",
     description="This is an example item.",
     price=19.99,
     currency="USD"
)

item2 = Item.objects.create(
     name="Example Item 2",
     description="This is an example item.",
     price=11.99,
     currency="USD"
)

item3 = Item.objects.create(
     name="Example Item 3",
     description="This is an example item.",
     price=39.99,
     currency="EUR"
)

from payments.models import Discount
discount = Discount.objects.create(
     code="32LZkEGQ"
)

from payments.models import Tax
tax = Tax.objects.create(
     name="VAT",
     percentage="20",
     jurisdiction="US"
)

from payments.models import Order
order = Order.objects.create(
    currency="USD"
)
order.items.add(item1, item2)
order.tax = tax
order.discount = discount
order.save()
EOF

echo "Starting server..."
python stripe_demo/manage.py runserver 0.0.0.0:$PORT