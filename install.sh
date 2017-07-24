#!/bin/bash

sudo apt-get update

sudo ./conf/configure_python.sh
sudo ./conf/configure_usb.sh
sudo ./conf/configure_nginx.sh
sudo ./conf/configure_motion.sh

./conf/configure_services.sh