# Django API

A Django + Django REST API, used as a backend for a cinema ticket website.

## Development

### Run tests

```sh
docker-compose run --rm api python manage.py test
```

### Format code with Black

```sh
docker-compose run --rm api black .
```

### Run lint

```sh
docker-compose run --rm api flake8 .
```
