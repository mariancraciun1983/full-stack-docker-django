#!/usr/bin/env bash

echo "Loading fixtures"

./manage.py loaddata --app app_genres app_genres/fixtures/all.json
./manage.py loaddata --app app_movies app_movies/fixtures/all.json