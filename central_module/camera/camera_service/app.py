#!/usr/bin/python3

import json
import logging
import sys

import falcon
from object_detector import ObjectDetector

logger = logging.getLogger('Camera service')
handler = logging.StreamHandler()
handler.setLevel(logging.WARNING)
logger.addHandler(handler)
logger.handlers.extend(logging.getLogger("gunicorn.error").handlers)

logging.basicConfig(stream=sys.stdout,
                    level=logging.DEBUG,
                    format='[%(asctime)s] [%(process)s] [%(levelname)s] [%(name)s] %(message)s')

api = falcon.API()
object_detector = ObjectDetector()


class Detect(object):
    def on_get(self, req, resp):
        object_name = req.get_param('object')
        data = object_detector.detect(object_name)
        logger.info('Detect ' + str(data))
        resp.body = json.dumps(dict(data=data))
        resp.status = falcon.HTTP_200

api.add_route('/camera/detect', Detect())
