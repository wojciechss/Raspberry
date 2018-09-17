"""
Tests for Mini Driver Processor
"""

import unittest
from mock import patch
from controller.processors.mini_driver_processor import MiniDriverProcessor

LED_ON = '0:1;'.encode('utf-8')
LED_OFF = '0:0;'.encode('utf-8')


class TestMiniDriverProcessor(unittest.TestCase):

    @patch('controller.processors.mini_driver_processor.serial')
    def test_should_turn_led_on(self, serial_mock):
        uut = MiniDriverProcessor()
        uut.ser = serial_mock

        uut.led_on()

        serial_mock.write.assert_called_once_with(LED_ON)

    @patch('controller.processors.mini_driver_processor.serial')
    def test_should_turn_led_off(self, serial_mock):
        uut = MiniDriverProcessor()
        uut.ser = serial_mock

        uut.led_off()

        serial_mock.write.assert_called_once_with(LED_OFF)

    @patch('controller.processors.mini_driver_processor.serial')
    def test_should_drive(self, serial_mock):
        left_speed = 22
        right_speed = 33
        uut = MiniDriverProcessor()
        uut.ser = serial_mock

        uut.drive(left_speed, right_speed)

        serial_mock.write.assert_called_once_with('1:22:33;'.encode('utf-8'))
