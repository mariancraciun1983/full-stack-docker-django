#!/usr/bin/env bash

wait-for-it -h mailer.service -p 25 -t 60 -- echo 'Mailer is UP' \
      && wait-for-it -h redis.service -p 6379 -t 60 -- echo 'Redis is UP' \
      && wait-for-it -h mysql.service -p 3306 -t 60 -- echo 'MySQL is UP' \
      && pipenv run celery -A config worker -l info