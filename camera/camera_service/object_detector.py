#!/usr/bin/python3

from image_analyzer import ImageAnalyzer
from stream_reader import StreamReader


class ObjectDetector:

    stream_url = 'http://samantha:8081/?action=stream'

    def __init__(self):
        self.stream_reader = StreamReader(self.stream_url)
        self.image_analyzer = ImageAnalyzer()

    def detect(self):
        img = self.stream_reader.read()
        return self.image_analyzer.analyze(img)
