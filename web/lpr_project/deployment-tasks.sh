#!/bin/bash

# collect static files
python manage.py compilescss
python manage.py collectstatic --noinput --ignore=*.scss
python manage.py compilescss --delete-files

#migrations
python manage.py migrate
python manage.py makemigrations accounts_app news_app people_app principles_app
python manage.py migrate

#populating database
./fixtures/aply_all.sh
