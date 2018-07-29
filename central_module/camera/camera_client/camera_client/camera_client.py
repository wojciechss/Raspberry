#!/usr/bin/python3

import json
import requests


class CameraClient:

    base_url = 'http://localhost:5003/camera'
    detect_url = base_url + '/detect'

    def detect(self, object):
        data = dict(object=object)
        r = requests.get(self.detect_url, params=data, verify=False)
        r.raise_for_status()
        return json.loads(r.content.decode('utf-8'))['data']
