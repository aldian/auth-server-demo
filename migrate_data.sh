#!/usr/bin/env bash

cd django
python3 manage.py makemigrations
python3 manage.py migrate
