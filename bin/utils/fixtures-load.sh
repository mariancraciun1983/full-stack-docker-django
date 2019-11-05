#!/usr/bin/env bash

echo "Loading fixtures"

# Created using  ./manage.py dumpdata --indent 2 app_user > app_user/fixtures/all.json
# Created using  ./manage.py dumpdata --indent 2 app_genres > app_genres/fixtures/all.json
# Created using  ./manage.py dumpdata --indent 2 app_movies > app_movies/fixtures/all.json

./manage.py loaddata --app app_user app_user/fixtures/all.json
./manage.py loaddata --app app_genres app_genres/fixtures/all.json
./manage.py loaddata --app app_movies app_movies/fixtures/all.json