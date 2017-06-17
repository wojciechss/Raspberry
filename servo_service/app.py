#!/usr/bin/python3

import falcon

from servo import Servo
PAN_PWM_PIN = 23

api = falcon.API()

servo = Servo()


class SetPanPosition(object):
    def on_get(self, req, resp):
        position = req.get_param('position')
        servo.set_pan_position(int(position))
        #print('Servo: ' + position)
        resp.status = falcon.HTTP_200

api.add_route('/servo/pan', SetPanPosition())


class SetTiltPosition(object):
    def on_get(self, req, resp):
        position = req.get_param('position')
        servo.set_tilt_position(int(position))
        #print('Servo: ' + position)
        resp.status = falcon.HTTP_200

api.add_route('/servo/tilt', SetPanPosition())
