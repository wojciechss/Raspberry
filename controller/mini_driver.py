#!/usr/bin/python3

import serial
import time


# Input:       'device:device_specific_data;'
# Led:         '0:{state};' on - 1, off - 0
# Motor:       '1:{left_speed}:{right_speed};'
# Ultrasonic:  '2;'
# Servo:       '3:{position}'
class MiniDriver:

    portName = '/dev/ttyUSB0'

    def connect(self):
        self.ser = serial.Serial(
            port=self.portName,
            baudrate=9600,
            timeout=5
        )
        self.__wait_for_connection()
        self._blink_led()
        self.set_servo_position(180)

    def led_on(self):
        self._write('0:1;')

    def led_off(self):
        self._write('0:0;')

    def drive(self, left_speed, right_speed):
        data = '1' + ':' + str(left_speed) + ':' + str(right_speed) + ';'
        self._write(data)

    def get_distance_request(self):
        self._write('2;')

    def read_distance(self):
        x = self._read_line()
        val = str(x, 'ascii')
        if self.__isInt(val):
            return self.__parseInt(val)
        return 0

    def set_servo_position(self, position):
        data = '3' + ':' + str(position) + ';'
        self._write(data)

    def _write(self, data):
        self.ser.write(data.encode('utf-8'))

    def _read_line(self):
        return self.ser.readline()

    def _blink_led(self):
        self.led_on()
        time.sleep(0.5)
        self.led_off()
        time.sleep(0.5)
        self.led_on()
        time.sleep(0.5)
        self.led_off()

    @classmethod
    def __wait_for_connection(cls):
        print('Waiting')
        time.sleep(10)
        print('Connected')

    @classmethod
    def __parseInt(cls, input):
        try:
            return int(input)
        except ValueError:
            pass

    @classmethod
    def __isInt(cls, value):
        try:
            int(value)
            return True
        except:
            return False
