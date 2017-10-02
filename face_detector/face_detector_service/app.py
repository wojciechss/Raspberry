#!/usr/bin/python3

import json
import logging
import sys

import falcon
from face_detector import FaceDetector

logger = logging.getLogger('Face detector service')
handler = logging.StreamHandler()
handler.setLevel(logging.WARNING)
logger.addHandler(handler)
logger.handlers.extend(logging.getLogger("gunicorn.error").handlers)

logging.basicConfig(stream=sys.stdout,
                    level=logging.DEBUG,
                    format='[%(asctime)s] [%(process)s] [%(levelname)s] [%(name)s] %(message)s')

api = falcon.API()
face_detector = FaceDetector()

class Face(object):
    def on_get(self, req, resp):
        data = face_detector.detect_face()
        logger.info('Detect face ' + str(data))
        resp.body = json.dumps(dict(data=data))
        resp.status = falcon.HTTP_200

api.add_route('/face_detector/detect', Face())