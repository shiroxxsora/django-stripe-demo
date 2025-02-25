#!/bin/bash

echo "Running migrations..."
python stripe_demo/manage.py migrate --noinput

echo "Starting server..."
python stripe_demo/manage.py runserver 0.0.0.0:$PORT