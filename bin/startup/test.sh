#!/usr/bin/env bash

wait-for-it -h $REDIS_HOST -p $REDIS_PORT -t 60 -- echo 'Redis is UP'
wait-for-it -h $MYSQL_HOST -p $MYSQL_PORT -t 60 -- echo 'MySQL is UP'
pipenv run flake8 . \
    && pipenv run coverage run manage.py test --failfast --keepdb --debug-mode -v 2