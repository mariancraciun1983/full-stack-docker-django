#!/usr/bin/env bash

echo "Cleaning up all migrations"

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete


echo "Now you need to execute
    python manage.py makemigrations
    python manage.py migrate
"