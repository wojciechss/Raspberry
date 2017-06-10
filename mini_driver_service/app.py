#!/usr/bin/python3

import json
import falcon
import logging

from mini_driver import MiniDriver

logger = logging.getLogger('Mini driver service')
api = falcon.API()
mini_driver = MiniDriver()


class LedOn(object):
    def on_get(self, req, resp):
        mini_driver.led_on()
        logger.info('Led on')
        resp.status = falcon.HTTP_200

api.add_route('/controller/led_on', LedOn())


class LedOff(object):
    def on_get(self, req, resp):
        mini_driver.led_off()
        logger.info('Led off')
        resp.status = falcon.HTTP_200

api.add_route('/controller/led_off', LedOff())


class Drive(object):
    def on_get(self, req, resp):
        left = req.get_param('left')
        right = req.get_param('right')
        mini_driver.drive(left, right)
        logger.info('Drive: ' + left + ':' + right)
        resp.status = falcon.HTTP_200

api.add_route('/controller/drive', Drive())


class ReadDistance(object):
    def on_get(self, req, resp):
        mini_driver.get_distance_request()
        distance = mini_driver.read_distance()
        logger.info('Distance: ' + str(distance))
        data = dict(distance=distance)
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(data)

api.add_route('/controller/ultrasonic', ReadDistance())


mini_driver.connect()
