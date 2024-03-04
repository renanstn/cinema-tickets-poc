# cinema-tickets-poc

[![Python](https://img.shields.io/badge/python-%2314354C.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-%23092E20.svg?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=flat&logo=django&logoColor=white&color=ff1709&labelColor=gray)](https://www.django-rest-framework.org/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=flat&logo=nginx&logoColor=white)](https://www.nginx.com/)
[![Insomnia](https://img.shields.io/badge/Insomnia-black?style=flat&logo=insomnia&logoColor=5849BE)](https://insomnia.rest/)


## Objective

This lab tries to implement a solution for a cinema tickets backend.

I used for study some concepts:

- Django / Django REST
- Celery (tasks and scheduler)
- Broker (RabbitMQ)
- Microservices


## File structure

This repo represents a microservice architecture, and has the following
structure:

```
.
└── root/
    ├── backend - Microservices in Django, FastAPI, etc.
    ├── infra - Dockerfiles containing settings for databases, brokers, etc.
    └── tools - Tool dumps, such as Insomnia.
```

## Services

This repo contains a `docker-compose` file centralizing all services:

- `database`: A PostgreSQL database;
- `broker`: A RabbitMQ instance;
- `nginx`: A Nginx instance;
- `api`: Contains a Django API built with `Django REST Framework`;
- `worker`: Contains a worker to process celery tasks on background;
- `scheduler`: Setup the schedule service to start periodic tasks on celery;
- `movies_api`: External service to get movie data from an external API.
