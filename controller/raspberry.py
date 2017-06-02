#!/usr/bin/python3

import time
from mini_driver import MiniDriver


class Raspberry:

    def __init__(self):
        self.mini_driver = MiniDriver()

    def run(self):
        self.mini_driver.connect()
        self.start_reading_data()

    def start_reading_data(self):
        isOn = False

        while 1:
            time.sleep(0.01)
            self.mini_driver.get_distance_request()
            distance = self.mini_driver.read_distance()
            if isOn == False and (distance > 0.0) and (distance < 20.0):
                self.mini_driver.led_on()
                isOn = True
            elif isOn == True and (distance > 20.0):
                self.mini_driver.led_off()
                isOn = False

if  __name__ =='__main__':
    Raspberry().run()
