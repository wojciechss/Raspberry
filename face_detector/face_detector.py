#!/usr/bin/python3

import json
import logging
from image_analyzer import ImageAnalyzer
from stream_reader import StreamReader
from controller_client.controller_client import ControllerClient


class FaceDetector:

    stream_url = 'http://localhost:8081/?action=stream'

    def __init__(self):
        self.logger = logging.getLogger('Obstacle detector')
        self.stream_reader = StreamReader()
        self.image_analyzer = ImageAnalyzer()
        self.controller_client = ControllerClient()

    def run(self):
        self.logger.info('Started face detection')
        while (True):
            self.detect_face()

    def detect_face(self):
        img = self.stream_reader.read(self.stream_url)
        data = self.image_analyzer.analyze(img)
        if len(data['content']) > 0:
            self.controller_client.report_event(json.dumps(data))
