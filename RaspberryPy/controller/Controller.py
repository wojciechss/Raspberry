#!/usr/bin/python3

from MiniDriver import MiniDriver
from flask import Flask, url_for

class Controller():

    def __init__(self):
        self.minidriver = MiniDriver()

    def run(self):
        self.minidriver.connect()

    def led_on(self):
        self.minidriver.led_on()

    def led_off(self):
        self.minidriver.led_off()

app = Flask(__name__)
controller = Controller()


@app.route('/led_on')
def led_on():
    controller.led_on()
    return 'on\n'

@app.route('/led_off')
def led_off():
    controller.led_off()
    return 'off\n'

if __name__ == '__main__':
    controller.run()
    app.run()