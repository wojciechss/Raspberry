#!/usr/bin/python3

import json
import requests


class FaceDetectorClient:

    base_url = 'http://localhost:5003/face_detector'
    detect_url = base_url + '/detect'

    def detect(self):
        r = requests.get(self.detect_url, verify=False)
        r.raise_for_status()
        return json.loads(r.content.decode('utf-8'))['data']
