#!/bin/bash

sudo apt-get update

sudo ./conf/configure_python.sh

sudo ./conf/create_service.sh analyzer_service analyzer_service
sudo ./conf/create_service.sh controller_service controller/controller_service
sudo ./conf/create_service.sh mini_driver_service mini_driver/mini_driver_service
sudo ./conf/create_service.sh nano_service nano/nano_service

echo 'Update USB rules'
sudo cp ./mini_driver/mini_driver_arduino/mini-driver-usb-serial.rules /etc/udev/rules.d
sudo cp ./nano/nano_arduino/nano-usb-serial.rules /etc/udev/rules.d

sudo ./conf/configure_nginx.sh

sudo ./conf/configure_motion.sh
