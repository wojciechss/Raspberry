#!/usr/bin/python3

import cv2


class FaceDetector:

    schema_path = '/opt/opencv/data/haarcascades/haarcascade_frontalface_default.xml'
    face_field = 'face'

    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(self.schema_path)

    def detect(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return self.face_cascade.detectMultiScale(gray, 1.3, 5)
