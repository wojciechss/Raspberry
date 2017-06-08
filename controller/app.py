#!/usr/bin/python3

import json
import falcon
import datetime

from controller import Controller

api = falcon.API()
controller = Controller()

def log(data):
    print(str(datetime.datetime.now()) + ':' + data)

class LedOn(object):
    def on_get(self, req, resp):
        controller.led_on()
        print('Led on')
        resp.status = falcon.HTTP_200  # This is the default status

api.add_route('/controller/led_on', LedOn())


class LedOff(object):
    def on_get(self, req, resp):
        controller.led_off()
        log('Led off')
        resp.status = falcon.HTTP_200  # This is the default status

api.add_route('/controller/led_off', LedOff())


class Drive(object):
    def on_get(self, req, resp):
        left = req.get_param('left')
        right = req.get_param('right')
        controller.drive(left, right)
        log('Drive: ' + left + ':' + right)
        resp.status = falcon.HTTP_200

api.add_route('/controller/drive', Drive())


class ReadDistance(object):
    def on_get(self, req, resp):
        controller.get_distance_request()
        distance = controller.read_distance()
        log('Distance: ' + str(distance))
        data = dict(distance=distance)
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(data)

api.add_route('/controller/ultrasonic', ReadDistance())


class SetServoPosition(object):
    def on_get(self, req, resp):
        position = req.get_param('position')
        controller.set_servo_position(position)
        log('Servo: ' + position)
        resp.status = falcon.HTTP_200

api.add_route('/controller/servo', SetServoPosition())

class InitData(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = json.dumps(Controller.get_initial_data())
    def on_post(self, req, resp):
        """Handles POST requests"""
        #Controller.save_initial_data(content)
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = ('OK')

api.add_route('/controller/init_data', InitData())

controller.run()
