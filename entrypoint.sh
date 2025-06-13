#!/bin/bash
set -e

# Executa as migrações e inicia o servidor
python manage.py collectstatic --noinput
python manage.py migrate

# Inicia o Gunicorn com binding para ECS
exec gunicorn titanic_project.wsgi:application \
    --bind 0.0.0.0:80 \
    --workers 4 \
    --threads 2 \
    --timeout 120
