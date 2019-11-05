#!/usr/bin/env bash

pipenv run flower --broker=redis://redis.service:6379/0 --port=8080