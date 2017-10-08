#!/usr/bin/python3

from face_detector import FaceDetector
from stream_reader import StreamReader


class ObjectDetector:

    stream_url = 'http://samantha:8081/?action=stream'

    def __init__(self):
        self.stream_reader = StreamReader(self.stream_url)
        self.face_detector = FaceDetector()

    def detect(self, object):
        img = self.stream_reader.read()
        print(object)
        return self.face_detector.run(img)
