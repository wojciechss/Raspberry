#!/usr/bin/python3

import json

from mini_driver import MiniDriver
from pan_tilt import ServoPWM

PAN_PWM_PIN = 23


class Controller:

    def __init__(self):
        self.mini_driver = MiniDriver()
        self.pan_servo = ServoPWM(PAN_PWM_PIN, (45.0, 1850), (90.0, 1400), (135.0, 1000.0))

    def run(self):
        self.mini_driver.connect()

    def led_on(self):
        self.mini_driver.led_on()

    def led_off(self):
        self.mini_driver.led_off()

    def drive(self, left_speed, right_speed):
        self.mini_driver.drive(left_speed, right_speed)

    def get_distance_request(self):
        self.mini_driver.get_distance_request()

    def read_distance(self):
        return self.mini_driver.read_distance()

    def set_servo_position(self, position):
        self.pan_servo.set_angle(position)

    @classmethod
    def get_initial_data(cls):
        with open('init_data.json') as data_file:
            initial_data = json.load(data_file)
        return initial_data

    @classmethod
    def save_initial_data(cls, data):
        with open('init_data.json', 'w') as outfile:
            json.dump(data, outfile)
