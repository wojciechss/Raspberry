#!/usr/bin/python3

import json
import falcon
import logging

from nano import Nano

logger = logging.getLogger('Nano service')
api = falcon.API()
nano = Nano()


class LedOn(object):
    def on_get(self, req, resp):
        nano.led_on()
        logger.info('Led on')
        resp.status = falcon.HTTP_200

api.add_route('/nano/led_on', LedOn())


class LedOff(object):
    def on_get(self, req, resp):
        nano.led_off()
        logger.info('Led off')
        resp.status = falcon.HTTP_200

api.add_route('/nano/led_off', LedOff())


class ReadDistance(object):
    def on_get(self, req, resp):
        nano.get_distance_request()
        distance = nano.read_distance()
        logger.info('Distance: ' + str(distance))
        data = dict(distance=distance)
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(data)

api.add_route('/nano/ultrasonic', ReadDistance())


class SetPanPosition(object):
    def on_get(self, req, resp):
        position = req.get_param('position')
        logger.info('Pan position: ' + str(position))
        nano.set_pan_position(int(position))
        resp.status = falcon.HTTP_200

api.add_route('/nano/pan', SetPanPosition())


class SetTiltPosition(object):
    def on_get(self, req, resp):
        position = req.get_param('position')
        logger.info('Tilt position: ' + str(position))
        nano.set_tilt_position(int(position))
        resp.status = falcon.HTTP_200

api.add_route('/nano/tilt', SetTiltPosition())


nano.connect()
