#!/usr/bin/python3

from image_analyzer import ImageAnalyzer
from mini_driver_client.mini_driver_client import MiniDriverClient


class FaceDetector:

    FILENAME = '/var/lib/motion/lastsnap.jpg'

    def __init__(self):
        self.image_analyzer = ImageAnalyzer(self.FILENAME)
        self.mini_driver_client = MiniDriverClient()

    def detect_face(self):
        if self.image_analyzer.is_face_detected():
            self.mini_driver_client.led_on()
        else:
            self.mini_driver_client.led_off()
