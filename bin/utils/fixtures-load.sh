#!/usr/bin/env bash

echo "Loading fixtures"

./manage.py loaddata --app auth.User fixtures/auth.User.json
./manage.py loaddata --app app_user fixtures/app_user.json
./manage.py loaddata --app app_genres fixtures/app_genres.json
./manage.py loaddata --app app_movies fixtures/app_movies.json
./manage.py loaddata --app app_genres fixtures/app_genres.json
./manage.py loaddata --app app_cart fixtures/app_cart.json