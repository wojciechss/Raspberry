#!/usr/bin/python3

import sys
import json
import falcon
import logging

from nano import Nano

logger = logging.getLogger('Nano service')
handler = logging.StreamHandler()
handler.setLevel(logging.WARNING)
logger.addHandler(handler)
logger.handlers.extend(logging.getLogger("gunicorn.error").handlers)

logging.basicConfig(stream=sys.stdout,
                    level=logging.DEBUG,
                    format='[%(asctime)s] [%(process)s] [%(levelname)s] %(message)s')

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
    def on_post(self, req, resp):
        position = req.get_param('position')
        logger.info('Pan position: ' + str(position))
        nano.set_pan_position(int(position))
        resp.status = falcon.HTTP_200

api.add_route('/nano/pan', SetPanPosition())


class SetTiltPosition(object):
    def on_post(self, req, resp):
        position = req.get_param('position')
        logger.info('Tilt position: ' + str(position))
        nano.set_tilt_position(int(position))
        resp.status = falcon.HTTP_200

api.add_route('/nano/tilt', SetTiltPosition())


class ReadAccelerometer(object):
    def on_get(self, req, resp):
        nano.get_accelerometer_data_request()
        acc_data = nano.read_accelerometer_data()
        logger.info('Accelerometer: ' + str(acc_data))
        data = dict(data=acc_data)
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(data)

api.add_route('/nano/accelerometer', ReadAccelerometer())


class ReadKtir(object):
    def on_get(self, req, resp):
        nano.get_ktir_data_request()
        ktir_data = nano.read_ktir_data()
        logger.info('Ktir: ' + str(ktir_data))
        data = dict(data=ktir_data)
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(data)

api.add_route('/nano/ktir', ReadKtir())

nano.connect()
