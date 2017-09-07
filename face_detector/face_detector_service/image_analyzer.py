#!/usr/bin/python3

import cv2
from position_calculator import PositionCalculator


class ImageAnalyzer:

    SCHEMA_PATH = '/opt/opencv/data/haarcascades/haarcascade_frontalface_default.xml'
    FACE_FIELD = 'face'

    def __init__(self, filename):
        self.filename = filename
        self.face_cascade = cv2.CascadeClassifier(self.SCHEMA_PATH)
        self.position_calculator = PositionCalculator(section_size=0.75)

    def analyze(self):
        img = cv2.imread(self.filename)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        height = img.shape[0]
        width = img.shape[1]
        sections = []
        for (x, y, w, h) in faces:
            section = dict(horizontal=self.position_calculator.section(x, w, width),
                           vertical=self.position_calculator.section(y, h, height),
                           distance=self.position_calculator.distance(h, height))
            sections.append(section)

        return self.make_response(sections)

    def make_response(self, sections):
        return dict(type=self.FACE_FIELD, content=sections)
