#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: start.sh [ENVIRONMENT](development/production)"
    exit 1
fi

ENVIRONMENT=$1

if [ "$ENVIRONMENT" = "development" ]; then
    python manage.py runserver 0.0.0.0:8000

elif [ "$ENVIRONMENT" = "production" ]; then
    uvicorn \
        django_api.asgi:application
        --host 0.0.0.0 \
        --port 8000
fi
