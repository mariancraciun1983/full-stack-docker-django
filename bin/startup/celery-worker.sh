#!/usr/bin/env bash

wait-for-it -h mailer.service -p 25 -t 60 -- echo 'Mailer is UP' \
    && wait-for-it -h $REDIS_HOST -p $REDIS_PORT -t 60 -- echo 'Redis is UP' \
    && wait-for-it -h $MYSQL_HOST -p $MYSQL_PORT -t 60 -- echo 'MySQL is UP' \
      && pipenv run celery -A config worker -l info