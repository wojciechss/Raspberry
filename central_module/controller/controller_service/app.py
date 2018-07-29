#!/usr/bin/python3

import json
import logging
import sys

import falcon
from nano_client.nano_client import NanoClient
from mini_driver_client.mini_driver_client import MiniDriverClient
from analyzer import Analyzer

logger = logging.getLogger('Controller service')
handler = logging.StreamHandler()
handler.setLevel(logging.WARNING)
logger.addHandler(handler)
logger.handlers.extend(logging.getLogger("gunicorn.error").handlers)

logging.basicConfig(stream=sys.stdout,
                    level=logging.DEBUG,
                    format='[%(asctime)s] [%(process)s] [%(levelname)s] [%(name)s] %(message)s')

api = falcon.API()
analyzer = Analyzer()
nano_cli = NanoClient()
mini_driver_client = MiniDriverClient()
analyzer.run()

class Drive(object):
    def on_post(self, req, resp):
        left = req.get_param('left')
        right = req.get_param('right')
        mini_driver_client.drive(left, right)
        logger.info('Drive: ' + left + ':' + right)
        resp.status = falcon.HTTP_200

api.add_route('/controller/drive', Drive())


class Start(object):
    def on_get(self, req, resp):
        logger.info('start')
        analyzer.start()


api.add_route('/controller/start', Start())


class Stop(object):
    def on_get(self, req, resp):
        logger.info('stop')
        analyzer.stop()


api.add_route('/controller/stop', Stop())

class Status(object):
    def on_get(self, req, resp):
        logger.info('Status ' + str(analyzer.running))


api.add_route('/controller/status', Status())
