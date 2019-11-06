#!/usr/bin/env bash

echo "Loading fixtures"

./manage.py dumpdata --indent 2 auth.User > fixtures/auth.User.json
./manage.py dumpdata --indent 2 app_user > fixtures/app_user.json
./manage.py dumpdata --indent 2 app_genres > fixtures/app_genres.json
./manage.py dumpdata --indent 2 app_movies > fixtures/app_movies.json
./manage.py dumpdata --indent 2 app_cart > fixtures/app_cart.json
