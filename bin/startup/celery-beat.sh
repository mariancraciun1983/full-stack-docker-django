#!/usr/bin/env bash

wait-for-it -h redis.service -p 6379 -t 60 -- echo 'Redis is UP'  \
      && wait-for-it -h mysql.service -p 3306 -t 60 -- echo 'MySQL is UP'  \
      && pipenv run celery -A config beat -l info \
        --pidfile='/celerybeat/celerybeat.pid' \
        --schedule='/celerybeat/celerybeat-schedule' 