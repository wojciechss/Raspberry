#!/usr/bin/python3

import falcon

from servo import ServoPWM
PAN_PWM_PIN = 23

api = falcon.API()

pan_servo = ServoPWM(PAN_PWM_PIN, (45.0, 1850), (90.0, 1400), (135.0, 1000.0))


class SetPanPosition(object):
    def on_get(self, req, resp):
        position = req.get_param('position')
        pan_servo.set_angle(int(position))
        print('Servo: ' + position)
        resp.status = falcon.HTTP_200

api.add_route('/servo/pan', SetPanPosition())

pan_servo.init_channel()