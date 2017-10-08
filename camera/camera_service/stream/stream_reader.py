#!/usr/bin/python3

import numpy as np
import cv2
import requests


class StreamReader:

    def __init__(self, url):
        self.url = url

    def read(self):
        self.stream = requests.get(self.url, stream=True)
        bytes = b''
        while True:
            try:
                bytes += self.stream.raw.read(1024)
                a = bytes.find(b'\xff\xd8')
                b = bytes.find(b'\xff\xd9')
                if a != -1 and b != -1:
                    jpg = bytes[a:b + 2]
                    bytes = bytes[b + 2:]
                    img = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                    return img
            except ThreadError:
                print('error')
