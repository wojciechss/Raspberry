#!/usr/bin/python3

import json

from mini_driver import MiniDriver


class Controller:

    def __init__(self):
        self.minidriver = MiniDriver()

    def run(self):
        self.minidriver.connect()

    def led_on(self):
        self.minidriver.led_on()

    def led_off(self):
        self.minidriver.led_off()

    def drive(self, left_speed, right_speed):
        self.minidriver.drive(left_speed, right_speed)

    def get_distance_request(self):
        self.minidriver.get_distance_request()

    def read_distance(self):
        return self.minidriver.read_distance()

    def set_servo_position(self, position):
        self.minidriver.set_servo_position(position)

    @classmethod
    def get_initial_data(cls):
        with open('init_data.json') as data_file:
            initial_data = json.load(data_file)
        return initial_data

    @classmethod
    def save_initial_data(cls, data):
        with open('init_data.json', 'w') as outfile:
            json.dump(data, outfile)
