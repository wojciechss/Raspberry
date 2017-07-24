#!/bin/bash

# http://hintshop.ludvig.co.nz/show/persistent-names-usb-serial-devices/

echo 'Update USB rules'

sudo cp ./mini_driver/mini_driver_arduino/mini-driver-usb-serial.rules /etc/udev/rules.d
sudo cp ./nano/nano_arduino/nano-usb-serial.rules /etc/udev/rules.d
