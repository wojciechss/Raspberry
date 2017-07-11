#!/bin/bash

args=("$@")
service_name=${args[0]}
service_path=${args[1]}

echo Create ${service_name} from ${service_path}

sed "s:{DIR}:`pwd`:g;s:{USER}:`whoami`:g;s:{SERVICE_NAME}:${service_name}:g;s:{SERVICE_PATH}:${service_path}:g" ./conf/service > ./conf/${service_name}

sudo mv ./conf/${service_name} /etc/init.d/${service_name}
sudo chmod 755 /etc/init.d/${service_name}
sudo chown root:root /etc/init.d/${service_name}
sudo update-rc.d ${service_name} defaults