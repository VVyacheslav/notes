# Gather static files
FROM node:14.17 as build-static

COPY frontend /app

COPY Makefile /tmp/Makefile

WORKDIR /app
RUN make -f /tmp/Makefile build-static

# Build django
FROM python:3.8

WORKDIR /app/src

RUN apt-get update && \
    pip install --upgrade pip && \
    touch /var/run/uwsgi-touch-reload

COPY requirements /tmp/requirements
RUN cd /tmp/requirements && \
    pip install --no-cache-dir -r main.txt && \
    rm -r /tmp/requirements

COPY compose/django/uwsgi.ini /app/uwsgi.ini
COPY compose/django/scripts/ /app/
RUN chmod +x /app/*.sh

COPY backend /app/src
RUN python manage.py collectstatic --no-input
COPY --from=build-static /app/dist /app/src/static
