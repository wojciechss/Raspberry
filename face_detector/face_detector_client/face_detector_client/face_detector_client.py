#!/usr/bin/python3

import requests


class FaceDetectorClient:

    face_detector_url = 'http://localhost:5003/face'
    detect_url = face_detector_url + '/detect'

    def detect_face(self):
        r = requests.get(self.detect_url, verify=False)
        r.raise_for_status()
