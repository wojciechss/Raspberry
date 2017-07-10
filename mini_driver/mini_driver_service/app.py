#!/usr/bin/python3

import sys
import falcon
import logging

from mini_driver import MiniDriver

logger = logging.getLogger('Mini driver service')
handler = logging.StreamHandler()
handler.setLevel(logging.WARNING)
logger.addHandler(handler)
logger.handlers.extend(logging.getLogger("gunicorn.error").handlers)

logging.basicConfig(stream=sys.stdout,
                    level=logging.DEBUG,
                    format='[%(asctime)s] [%(process)s] [%(levelname)s] %(message)s')

api = falcon.API()
mini_driver = MiniDriver()


class LedOn(object):
    def on_get(self, req, resp):
        mini_driver.led_on()
        logger.info('Led on')
        resp.status = falcon.HTTP_200

api.add_route('/mini_driver/led_on', LedOn())


class LedOff(object):
    def on_get(self, req, resp):
        mini_driver.led_off()
        logger.info('Led off')
        resp.status = falcon.HTTP_200

api.add_route('/mini_driver/led_off', LedOff())


class Drive(object):
    def on_post(self, req, resp):
        left = req.get_param('left')
        right = req.get_param('right')
        mini_driver.drive(left, right)
        logger.info('Drive: ' + left + ':' + right)
        resp.status = falcon.HTTP_200

api.add_route('/mini_driver/drive', Drive())


mini_driver.connect()