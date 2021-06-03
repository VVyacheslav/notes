ARG DJANGO_IMAGE
FROM globaldots/django as django

FROM nginx:latest
COPY ./compose/nginx/site.conf.template /etc/nginx/conf.d/
COPY ./compose/nginx/start-nginx.sh /app/start-nginx.sh
RUN chmod +x /app/start-nginx.sh
CMD /app/start-nginx.sh

COPY --from=django /app/src/static /app/static
