# =============================================================================
# Base
# =============================================================================
FROM python:3.9 AS base
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN apt-get update && \
    pip install --upgrade pip && \
    pip install poetry
WORKDIR /app
COPY pyproject.toml poetry.lock /app/

# =============================================================================
# Development
# =============================================================================
FROM base AS development
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi
COPY . /app/
RUN chmod +x /app/scripts/*.sh
ENTRYPOINT [ "scripts/entrypoint.sh" ]
CMD [ "scripts/start.sh", "development" ]

# =============================================================================
# Production
# =============================================================================
FROM base AS production
RUN poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi
COPY . /app/
RUN chmod +x /app/scripts/*.sh
ENTRYPOINT [ "scripts/entrypoint.sh" ]
CMD [ "scripts/start.sh", "production" ]

# =============================================================================
# Worker
# =============================================================================
FROM base AS worker
RUN poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi
CMD ["celery", "-A", "core", "worker", "--loglevel=INFO"]

# =============================================================================
# Scheduler
# =============================================================================
FROM base as scheduler
RUN poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi
CMD ["celery", "-A", "core", "beat", "--loglevel=INFO"]
