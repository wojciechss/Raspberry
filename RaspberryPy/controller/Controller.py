#!/usr/bin/python3

from MiniDriver import MiniDriver
from flask import Flask, url_for
from flask import request
from flask.json import dumps, JSONEncoder

class Controller():

    def __init__(self):
        self.minidriver = MiniDriver()

    def run(self):
        self.minidriver.connect()

    def led_on(self):
        self.minidriver.led_on()

    def led_off(self):
        self.minidriver.led_off()

    def get_distance_request(self):
        self.minidriver.get_distance_request()

    def read_distance(self):
        return self.minidriver.read_distance()

    def drive(self, left_speed, right_speed):
        self.minidriver.drive(left_speed, right_speed)

app = Flask(__name__)
controller = Controller()


@app.route('/controller/led_on')
def led_on():
    controller.led_on()
    return 'on\n'

@app.route('/controller/led_off')
def led_off():
    controller.led_off()
    return 'off\n'

@app.route('/controller/drive')
def drive():
    left = request.args.get('left')
    right = request.args.get('right')
    print(left)
    print(right)
    #controller.drive(left, right)
    return 'drive\n'

@app.route('/controller/ultrasonic')
def read_distance():
    controller.get_distance_request()
    distance = controller.read_distance()
    data = dict(distance=distance)
    return dumps(data)

if __name__ == '__main__':
    #controller.run()
    app.run()