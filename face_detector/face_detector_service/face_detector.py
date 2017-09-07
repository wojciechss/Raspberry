#!/usr/bin/python3

import json
from image_analyzer import ImageAnalyzer
from controller_client.controller_client import ControllerClient


class FaceDetector:

    FILENAME = '/var/lib/motion/lastsnap.jpg'

    def __init__(self):
        self.image_analyzer = ImageAnalyzer(self.FILENAME)
        self.controller_client = ControllerClient()

    def detect_face(self):
        data = self.image_analyzer.analyze()
        if len(data['content']) > 0:
            self.controller_client.report_event(json.dumps(data))
