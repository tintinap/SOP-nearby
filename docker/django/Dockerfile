FROM python:3.7.3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY base.py /usr/local/lib/python3.7/site-packages/django/db/backends/mysql/
COPY operations.py /usr/local/lib/python3.7/site-packages/django/db/backends/mysql/
