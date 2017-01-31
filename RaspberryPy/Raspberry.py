#!/usr/bin/python3

import serial
import time

class Raspberry:

    portName = '/dev/ttyUSB0'

    def run(self):
        self.__connect()

    def __connect(self):
        self.ser = serial.Serial(
            port = self.portName,
            baudrate = 9600,
            timeout = 5
        )
        self.__wait_for_connection()
        self.read_data()

    @classmethod
    def __wait_for_connection(cls):
        print('Waiting')
        time.sleep(10)
        print('Connected')

    @classmethod
    def __parseFloat(cls, input):
        try:
            return float(input)
        except ValueError:
            pass

    @classmethod
    def __isfloat(cls, value):
        try:
            float(value)
            return True
        except:
            return False

    def __get_distance(self):
        self.ser.write(b'read;')
        x = self.ser.readline()
        val = str(x, 'ascii')
        if self.__isfloat(val):
            return self.__parseFloat(val)

    def read_data(self):
        isOn = False

        while 1:
            time.sleep(0.01)
            distance = self.__get_distance()
            if isOn == False and (distance > 0.0) and (distance < 20.0):
                self.ser.write(b'on;')
                isOn = True
            elif isOn == True and (distance > 20.0):
                self.ser.write(b'off;')
                isOn = False

def main():
    Raspberry().run()


if  __name__ =='__main__':
    main()