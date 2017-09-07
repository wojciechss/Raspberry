#!/usr/bin/python3

import sys
import falcon
import logging

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

print(OPENCV_PATH)
face_detector = FaceDetector()


class DetectFace(object):
    def on_get(self, req, resp):
        face_detector.detect_face()
        resp.status = falcon.HTTP_200

api.add_route('/face/detect', DetectFace())
