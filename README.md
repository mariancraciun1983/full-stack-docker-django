<h1 align="center">Fullstack Django</h1>

<div align="center">
  <a href="https://travis-ci.org/mariancraciun1983/full-stack-docker-django">
    <img src="https://secure.travis-ci.org/mariancraciun1983/full-stack-docker-django.svg?branch=master" alt="Travis CI" />
  </a>
  <a href="https://coveralls.io/r/mariancraciun1983/full-stack-docker-django">
    <img src="https://img.shields.io/coveralls/mariancraciun1983/full-stack-docker-django?branch=master&style=flat" alt="Coverage Status" />
  </a>
  <a href="https://pyup.io/account/repos/github/mariancraciun1983/full-stack-docker-django/">
    <img src="https://pyup.io/repos/github/mariancraciun1983/full-stack-docker-django/shield.svg" alt="pyup updates" />
  </a>
  <a href="https://pyup.io/account/repos/github/mariancraciun1983/full-stack-docker-django/">
    <img src="https://pyup.io/repos/github/mariancraciun1983/full-stack-docker-django/python-3-shield.svg" alt="pyup python 3" />
  </a>

  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License" />
  </a>
</div>

This repo is meant to provide you a foundation for a new django base project. It saves you time as it has some ready made apps, components and integrations.
I is also part of the [full-stack-docker-compose](https://github.com/mariancraciun1983/full-stack-docker-compose)

The most relevant parts provided by this repo are:
 - pipenv - requirements and venv management
 - celery and celery-beat integration and async and cron tasks
 - api - using django rest
 - fixtures - preloaded json with sample data
 - tests - unit and integration tests for some of the apps
 - tasks - cli tasks
 - liting - pytlint
 - env vars - loaded via docker-compose vars
 - ci - travis/coverage and pyup integration


# TL;DR
Want to get you hands on the code?
```bash

# Make sure you've got pipenv installed
pip install pipenv

# Clone the repo
git clone git@github.com:mariancraciun1983/full-stack-docker-django.git
cd full-stack-docker-django

# Pipenv install the deps
pipenv install
# Activate the installed env
pipenv shell

# Edit the .env file with the mysql and redis connection settings
cp .env.example .env
vim .env

# Load the env variables from .env
source .env

# Migrate
python manage.py migrate
# Load fixtures
./bin/utils/fixtures-load.sh

# Start the dev server
python manage.py runserver 0.0.0.0:8000


```

# Project layout
The project is made of the following structure 
 - apps - prefixed with **app\_** ( [app_auth](./app_auth), [app_auth](./app_auth) ..etc ) 
 - utilies - [base](./base) folder with various modules that could be used in this project
 - config - [config](./config) which contains the settings modules (local/test), celery, wsgi and urls configurations
 - pipfiles - Pipfile and Pipfile.lock files used by pipenv
 - configurations - .dot files used by git coverage ... etc.
There is no "main" app, as it's used with django projects.

## Configuration

Based on the ```DJENV``` environment variable the local or test configuration can be loaded. There is a common.py which is exended by each config.

The [celery.py](./config/celery.py) contains the celery configuration

The urls configuration is split into a base [urls.py](./config/urls.py) and [urls_api.py](./config/urls_api.py) used by the APIs.

manage.py and wsgi.py are configured to use the DJENV env variable in order to load the appropriate configuration.


# Pipenv
Pipenv is a tool similar with npm and nvm and it allows you to manage package dependencies and python versions. In order to create the virtual environment and install it's packages you need to run ```pipenv install```. To activate the environment, run ```pipenv shell```.

# Celery
Celery is a distributed task queue and it's integration with django via tasks/async tasks. Usually these tasks are placed inside of the tasks.py files. Specifically in this project, there is a mailer integration in the auth (register/forgot) app.

Celery beat is used to manage cron tasks. In this project it's possible to configure the tasks via the CELERY_BEAT_SCHEDULE settings or via the admin (django admin) interface.

# API
Django REST framework is integrated and configured via settings. Each app contains an api folder (ex: [app_genres/api](./app_genres/api) ). Each of these apis endpoints are being combined into a single one under /api, where you can find a browsable list.
The APIs are created to provide the data for a similar app, but as a SOA. 
For authentication, JWT is provided to via a custom [JWTAuthentication](./base/api/token.py) middleware which is a more simplified version of the classical JWT authentications.


# URLS
The main configuration is [urls.py](./config/urls.py) which includes the urls from each app and the urls from each app apis. A basic schema for the URLs, with a depth=2 is as
- /
- /movies
- /cart
- /auth
- /api
  - /api/movies
  - /api/cart
  - /api/auth


# Fixtures
Fixtures are found in the /fixtures folder and helper scripts to load and dump them are found in the ./bin/utils folder.

```bash
# Dump
./manage.py dumpdata --indent 2 app_genres > fixtures/app_genres.json
# Load
./manage.py loaddata --app app_genres fixtures/app_genres.json

```

# Tests and Linting
The tests are found in the test.py files and provide a basic example of unit and integration testing.
They are found in both apps and apps/api folders.
Bacause the tests are runnin on views too which should work with data, fixtures are configured too to be automatically loaded.

```bash
# if the shell is activated
manage.py test --failfast --keepdb --debug-mode -v 2
# if the pipenv shell is not activated
pipenv run manage.py test --failfast --keepdb --debug-mode -v 2
# run with coverage
pipenv run coverage run manage.py test --failfast --keepdb --debug-mode -v 2
```
The ```coverage html``` could be run to generate the html report under coverage_html_report by using the information from .coverage.

Liting is configured in the setup.cfg file and can be run with:

```bash
flake8 .
# or if the pipenv shell is not activated
pipenv run flake8 .
```

# ENV
The environment variables required are

```bash
DJENV=local

REDIS_HOST=localhost
REDIS_PORT=6379

MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_NAME=fsd
MYSQL_NAME_TEST=fsd_test
MYSQL_USER=user
MYSQL_PASSWORD=pass
```


# CI
TravisCI is being used for running tests and it's configuration is found at [.travis.yml](./.travis.yml)

# Other things to know

This project is depending on services and configurations provided in the [full-stack-docker-compose](https://github.com/mariancraciun1983/full-stack-docker-compose) project. Howeve, if you check the .travis.yml you will see how you can run the code anywhere else (where docker/docker-compose isn't available).

[wait-for-it](https://github.com/vishnubob/wait-for-it) is being used to wait for mysql and redis to become available. Usually under docker-compose, you start all services, however, mysql takes more to load than it does for django to start. During this time, django will crash as the db is not available.
In order to solve this, the following code can be used:

```bash
#!/usr/bin/env bash
wait-for-it -h redis.service -p 6379 -t 60 -- echo 'Redis is UP' \
    && wait-for-it -h mysql.service -p 3306 -t 60 -- echo 'MySQL is UP' \
    && pipenv run  python manage.py migrate \
    && pipenv run  python manage.py runserver 0.0.0.0:8000

```

.vscode and .devcontainer configured for Visual Studio Code integration (linting ..etc)

The code does not contain a Production environment yet.