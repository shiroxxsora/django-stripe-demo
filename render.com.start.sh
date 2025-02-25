#!/bin/bash

echo "Running migrations..."
python stripe_demo/manage.py migrate --noinput

echo "Collecting static files..."
python stripe_demo/manage.py collectstatic --noinput

echo "Starting Gunicorn server..."
gunicorn stripe_demo.wsgi:application --bind 0.0.0.0:$PORT