#!/bin/bash

# collect static files
python manage.py compilescss
python manage.py collectstatic --dry-run --noinput --ignore=*.scss
python manage.py compilescss --delete-files

#migrations
python manage.py migrate
python manage.py makemigrations accounts_app news_app people_app principles_app
python manage.py migrate

#populating database
python manage.py loaddata fixtures/users.json fixtures/reforms_ready.json fixtures/qa.json fixtures/principles.json fixtures/people.json fixtures/opinions.json fixtures/news.json fixtures/structures.json
