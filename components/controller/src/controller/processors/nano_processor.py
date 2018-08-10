#!/usr/bin/python3

import time
import serial


# Input:         'device:device_specific_data;'
# Led:           '0:{state};' on - 1, off - 0
# Ultrasonic:    '1;'
# Servo:         '2;{device}:{position}' pan - 0, tilt - 1
# Accelerometer: '3;'
# Ktir:          '4;'
class NanoProcessor:

    portName = '/dev/nanoBoard'

    def __init__(self):
        self.ser = serial.Serial(
            port=self.portName,
            baudrate=9600,
            timeout=5
        )

    def connect(self):
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
        val = str(self._read_line(), 'ascii')
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
        return str(self._read_line(), 'ascii')

    def get_ktir_data_request(self):
        self._write('4;')

    def read_ktir_data(self):
        return str(self._read_line(), 'ascii')

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
    def __parse_int(cls, input_val):
        try:
            return int(input_val)
        except ValueError:
            pass

    @classmethod
    def __is_int(cls, value):
        try:
            int(value)
            return True
        except:
            return False
