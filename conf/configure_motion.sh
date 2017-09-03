#!/bin/bash

# http://www.instructables.com/id/Raspberry-Pi-remote-webcam/
# http://www.instructables.com/id/Remote-Control-Camera-by-Raspberry-Pi/

echo 'Configure motion'

apt-get install motion

cp ./conf/motion /etc/default/motion
cp ./conf/motion.conf /etc/motion/motion.conf
cp ./face_detector/face_detector_client/detect_face /usr/local/bin

# modprobe bcm2835-v4l2 in /etc/rc.local to make it run on every boot automatically.

cp ./conf/rc.local /etc

chmod 777 /var/lib/motion