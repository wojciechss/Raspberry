#!/usr/bin/python3

import logging
import cv2

class FaceDetector:

    logger = logging.getLogger('Face detector')
    handler = logging.StreamHandler()
    handler.setLevel(logging.WARNING)
    logger.addHandler(handler)
    logger.handlers.extend(logging.getLogger("gunicorn.error").handlers)

    def __init__(self, filename):
        self.filename = filename
        self.face_cascade = cv2.CascadeClassifier('/home/wojtek/opencv/opencv/data/haarcascades/haarcascade_frontalface_default.xml')

    def is_face_detected(self):
        img = cv2.imread(self.filename)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            return True
        return False
