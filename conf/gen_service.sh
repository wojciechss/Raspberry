#!/bin/bash

args=("$@")
service_name=${args[0]}
service_path=${args[1]}
echo ${service_name}
echo ${service_path}

sed "s:{DIR}:`pwd`:g;s:{USER}:`whoami`:g;s:{SERVICE_NAME}:${service_name}:g;s:{SERVICE_PATH}:${service_path}:g" ./conf/service > ./conf/${service_name}
