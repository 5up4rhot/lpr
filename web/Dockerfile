FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /lpr_project
WORKDIR /lpr_project
COPY requirements.txt /lpr_project/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /lpr_project/
