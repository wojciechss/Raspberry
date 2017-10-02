#!/bin/bash

echo 'Create services'

./conf/create_service.sh controller_service controller/controller_service
./conf/create_service.sh mini_driver_service mini_driver/mini_driver_service
./conf/create_service.sh nano_service nano/nano_service
./conf/create_service.sh face_detector_service face_detector/face_detector_service
