#!/bin/bash

args=("$@")
service_name=${args[0]}

echo Create ${service_name}

sudo cp ./conf/service /etc/init.d/${service_name}
sudo chmod 755 /etc/init.d/${service_name}
sudo chown root:root /etc/init.d/${service_name}
sudo update-rc.d ${service_name} defaults