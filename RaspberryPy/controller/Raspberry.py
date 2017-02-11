#!/usr/bin/python3

import time
from MiniDriver import MiniDriver

class Raspberry:

    def __init__(self):
        self.minidriver = MiniDriver()

    def run(self):
        self.minidriver.connect()
        self.start_reading_data()

    def start_reading_data(self):
        isOn = False

        while 1:
            time.sleep(0.01)
            self.minidriver.get_distance_request()
            distance = self.minidriver.read_distance()
            if isOn == False and (distance > 0.0) and (distance < 20.0):
                self.minidriver.led_on()
                isOn = True
            elif isOn == True and (distance > 20.0):
                self.minidriver.led_off()
                isOn = False

if  __name__ =='__main__':
    Raspberry().run()