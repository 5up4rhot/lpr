# pull official base image
FROM python:3.7

# set work directory
RUN mkdir /lpr_web_prod
WORKDIR /lpr_web_prod/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 1

# install dependencies
COPY ./requirements.txt /lpr_web_prod/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project
COPY . /lpr_web_prod/
WORKDIR /lpr_web_prod/lpr_project/
