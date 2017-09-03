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

FILENAME = 'lastsnap.jpg'
api = falcon.API()
face_detector = FaceDetector(FILENAME)


class DetectFace(object):
    def on_get(self, req, resp):
        detected = face_detector.is_face_detected()
        logger.info('Face detected ' + detected)
        resp.status = falcon.HTTP_200

api.add_route('/face/detect', DetectFace())
