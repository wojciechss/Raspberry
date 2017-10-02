#!/usr/bin/python3

import json
import logging
from image_analyzer import ImageAnalyzer
from stream_reader import StreamReader


class FaceDetector:

    stream_url = 'http://localhost:8081/?action=stream'

    def __init__(self):
        self.logger = logging.getLogger('Face detector')
        self.stream_reader = StreamReader()
        self.image_analyzer = ImageAnalyzer()

    def detect_face(self):
        img = self.stream_reader.read(self.stream_url)
        return self.image_analyzer.analyze(img)
