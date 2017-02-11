#!/usr/bin/python3

import serial
import time

class MiniDriver:

    portName = '/dev/ttyUSB0'

    def connect(self):
        self.ser = serial.Serial(
            port=self.portName,
            baudrate=9600,
            timeout=5
        )
        self.__wait_for_connection()

    def led_on(self):
        self._write(b'on;')

    def led_off(self):
        self._write(b'off;')

    def get_distance_request(self):
        self._write(b'read;')

    def read_distance(self):
        x = self._readline()
        val = str(x, 'ascii')
        if self.__isfloat(val):
            return self.__parseFloat(val)

    def _write(self, data):
        self.ser.write(data)

    def _readline(self):
        return self.ser.readline()

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