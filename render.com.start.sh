#!/bin/bash

echo "Running migrations..."
python stripe_demo/manage.py migrate --noinput

echo "Starting Gunicorn server..."
gunicorn stripe_demo/manage.py runserver 0.0.0.0:$PORT