#!/bin/bash

echo 'Install python dependencies'
sudo pip3 install -r requirements.txt

echo 'Create services'

echo 'Create analyzer service'
./conf/gen_service.sh analyzer_service analyzer_service
sudo mv ./conf/analyzer_service /etc/init.d/analyzer_service
sudo chmod 755 /etc/init.d/analyzer_service
sudo update-rc.d analyzer_service defaults

echo 'Create controller service'
./conf/gen_service.sh controller_service controller/controller_service
sudo mv ./conf/controller_service /etc/init.d/controller_service
sudo chmod 755 /etc/init.d/controller_service
sudo update-rc.d controller_service defaults

echo 'Create mini driver service'
./conf/gen_service.sh mini_driver_service mini_driver/mini_driver_service
sudo mv ./conf/mini_driver_service /etc/init.d/mini_driver_service
sudo chmod 755 /etc/init.d/mini_driver_service
sudo update-rc.d mini_driver_service defaults

echo 'Create nano service'
./conf/gen_service.sh nano_service nano/nano_service
sudo mv ./conf/nano_service /etc/init.d/nano_service
sudo chmod 755 /etc/init.d/nano_service
sudo update-rc.d nano_service defaults