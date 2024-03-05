#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: start.sh [ENVIRONMENT](development/production)"
    exit 1
fi

ENVIRONMENT=$1

if [ "$ENVIRONMENT" = "development" ]; then
    echo "Running app on development mode"
    python manage.py loaddata test
    python manage.py runserver 0.0.0.0:8000

elif [ "$ENVIRONMENT" = "production" ]; then
    echo "Running app on production mode"
    uvicorn django_api.asgi:application --host 0.0.0.0 --port 8000
fi
