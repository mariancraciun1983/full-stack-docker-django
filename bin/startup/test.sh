#!/usr/bin/env bash

wait-for-it -h redis.service -p 6379 -t 60 -- echo 'Redis is UP' \
    && wait-for-it -h mysql.service -p 3306 -t 60 -- echo 'MySQL is UP' \
    && pipenv run flake8 . \
    && pipenv run coverage run manage.py test --failfast --debug-mode -v 2 app_genres