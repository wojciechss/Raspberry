#!/usr/bin/python3

import serial
import time


# Input:       'device:device_specific_data;'
# Led:         '0:{state};' on - 1, off - 0
# Motor:       '1:{left_speed}:{right_speed};'
class MiniDriver:

    portName = '/dev/miniDriver'

    def connect(self):
        self.ser = serial.Serial(
            port=self.portName,
            baudrate=9600,
            timeout=5
        )
        self.__wait_for_connection()
        self._blink_led()

    def led_on(self):
        self._write('0:1;')

    def led_off(self):
        self._write('0:0;')

    def drive(self, left_speed, right_speed):
        data = '1' + ':' + str(left_speed) + ':' + str(right_speed) + ';'
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
