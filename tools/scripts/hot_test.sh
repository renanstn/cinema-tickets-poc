#!/bin/bash

# This script acts like a "hot reload" feature for developments.
# It runs all tests when any file is changed.
# To use this script, you must have inotify-tools installed on your machine:
# sudo apt install inotify-tools

LOOKUP_PATH="/home/renan/GitHub/cinema-tickets-poc"

while inotifywait -r -e modify --exclude '\.git|\.md|\.sh' $LOOKUP_PATH; do
    docker-compose run --rm api python manage.py test;
done
