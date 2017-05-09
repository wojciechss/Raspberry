#!/usr/bin/python3

import json
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

    @classmethod
    def get_initial_data(cls):
        with open('init_data.json') as data_file:
            initial_data = json.load(data_file)
        return initial_data

    @classmethod
    def save_initial_data(cls, data):
        with open('init_data.json', 'w') as outfile:
            json.dump(data, outfile)

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
    controller.drive(left, right)
    return 'drive\n'

@app.route('/controller/ultrasonic')
def read_distance():
    controller.get_distance_request()
    distance = controller.read_distance()
    data = dict(distance=distance)
    return dumps(data)

@app.route('/controller/init_data', methods=['GET', 'POST'])
def get_init_data():
    if request.method == 'GET':
        return dumps(Controller.get_initial_data())
    if request.method == 'POST':
        content = request.get_json()
        Controller.save_initial_data(content)
        return 'OK'

def https_app():
    import ssl
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain('server.crt', 'server.key')
    app.run(ssl_context=context)

if __name__ == '__main__':
    controller.run()
    https_app()