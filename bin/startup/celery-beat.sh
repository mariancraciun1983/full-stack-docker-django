#!/usr/bin/env bash

wait-for-it -h $REDIS_HOST -p $REDIS_PORT -t 60 -- echo 'Redis is UP' \
    && wait-for-it -h $MYSQL_HOST -p $MYSQL_PORT -t 60 -- echo 'MySQL is UP' \
      && pipenv run celery -A config beat -l info \
        --pidfile='/celerybeat/celerybeat.pid' \
        --schedule='/celerybeat/celerybeat-schedule' 