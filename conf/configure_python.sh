#!/bin/bash

echo 'Install python dependencies'

apt-get install python3-pip

pip3 install --upgrade pip
pip3 install -U setuptool
pip3 install -r ./conf/requirements.txt --upgrade
