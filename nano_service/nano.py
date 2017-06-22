#!/usr/bin/python3

import serial
import time


# Input:       'device:device_specific_data;'
# Led:         '0:{state};' on - 1, off - 0
# Ultrasonic:  '1;'
# Pan Servo:   '2:{position}'
# Tilt Servo:  '3:{position}'
class Nano:

    portName = '/dev/nanoBoard'

    def connect(self):
        self.ser = serial.Serial(
            port=self.portName,
            baudrate=9600,
            timeout=5
        )
        self.__wait_for_connection()
        self._blink_led()
        self.set_pan_position(160)
        self.set_tilt_position(100)

    def led_on(self):
        self._write('0:1;')

    def led_off(self):
        self._write('0:0;')

    def get_distance_request(self):
        self._write('1;')

    def read_distance(self):
        x = self._read_line()
        val = str(x, 'ascii')
        if self.__is_int(val):
            return self.__parse_int(val)
        return 0

    def set_pan_position(self, position):
        data = '2:0:' + str(position) + ';'
        self._write(data)

    def set_tilt_position(self, position):
        data = '2:1:' + str(position) + ';'
        self._write(data)

    def get_accelerometer_data_request(self):
        self._write('3;')

    def read_accelerometer_data(self):
        x = self._read_line()
        val = str(x, 'ascii')
        print(val)
        return val

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
    def __parse_int(cls, input):
        try:
            return int(input)
        except ValueError:
            pass

    @classmethod
    def __is_int(cls, value):
        try:
            int(value)
            return True
        except:
            return False
