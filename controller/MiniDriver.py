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
        self._write('led:on;')

    def led_off(self):
        self._write('led:off;')

    def drive(self, left_speed, right_speed):
        data = 'motor' + ':' + str(left_speed) + ':' + str(right_speed) + ';'
        self._write(data)

    def get_distance_request(self):
        self._write('ultrasonic;')

    def read_distance(self):
        x = self._readline()
        val = str(x, 'ascii')
        if self.__isfloat(val):
            return self.__parseFloat(val)
        return 0

    def _write(self, data):
        self.ser.write(data.encode('utf-8'))

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