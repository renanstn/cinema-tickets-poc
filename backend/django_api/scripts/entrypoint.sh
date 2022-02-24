#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate --noinput --check
python manage.py createadmin

exec "$@"
