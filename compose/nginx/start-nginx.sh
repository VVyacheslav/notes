#!/usr/bin/env bash


envsubst '$NGINX_SERVER_NAME' < /etc/nginx/conf.d/site.conf.template > /etc/nginx/conf.d/default.conf
nginx -g "daemon off;"
