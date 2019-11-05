#!/usr/bin/env bash

echo "Testing all apps"

./manage.py test --keepdb --failfast --keepdb --debug-mode -v 2
