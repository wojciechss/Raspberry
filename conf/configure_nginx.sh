#!/bin/bash

echo 'Configure nginx'

# sed "s:{DIR}:`pwd`:g;" ./conf/nginx.conf > /etc/nginx/nginx.conf
sed "s:{DIR}:`pwd`:g;" ./conf/nginx_http.conf > /etc/nginx/nginx.conf
