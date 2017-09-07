#!/usr/bin/python3

from image_analyzer import ImageAnalyzer
from controller_client.controller_client import ControllerClient


class FaceDetector:

    FILENAME = '/var/lib/motion/lastsnap.jpg'

    def __init__(self):
        self.image_analyzer = ImageAnalyzer(self.FILENAME)
        self.controller_client = ControllerClient()

    def detect_face(self):
        data = self.image_analyzer.analyze()
        self.controller_client.report_event(data)

