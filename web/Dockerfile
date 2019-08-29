# pull official base image
FROM python:3.7

# set work directory
RUN mkdir /web
WORKDIR /web/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 1

# install dependencies
COPY ./requirements.txt /web/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project
COPY . /web/
WORKDIR /web/lpr_project/

# collect static files
RUN python manage.py compilescss
RUN python manage.py collectstatic --noinput --ignore=*.scss
RUN python manage.py compilescss --delete-files

# add and run as non-root user
RUN adduser -uid 1000 myuser
USER myuser

# run gunicorn
CMD gunicorn lpr_project.wsgi:application --bind 0.0.0.0:$PORT
