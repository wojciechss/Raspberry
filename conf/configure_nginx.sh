#!/bin/bash

echo 'Configure nginx'

sed "s:{DIR}:`pwd`:g;" ./conf/nginx.conf > /etc/nginx/nginx.conf
