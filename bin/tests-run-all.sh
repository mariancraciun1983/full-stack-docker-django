#!/usr/bin/env bash

echo "Testing apps"

# Created using  ./manage.py dumpdata --indent 2 app_movies > app_movies/fixtures/all.json

coverage run manage.py test --keepdb --failfast --debug-mode -v 2 app_genres
