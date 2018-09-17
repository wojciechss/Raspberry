"""
Tests for Nano Processor
"""

import unittest
from mock import patch
from controller.processors.nano_processor import NanoProcessor

LED_ON = '0:1;'.encode('utf-8')
LED_OFF = '0:0;'.encode('utf-8')


class TestKeycloakImporter(unittest.TestCase):

    @patch('controller.processors.nano_processor.serial')
    def test_should_turn_led_on(self, serial_mock):
        uut = NanoProcessor()
        uut.ser = serial_mock

        uut.led_on()

        serial_mock.write.assert_called_once_with(LED_ON)

    @patch('controller.processors.nano_processor.serial')
    def test_should_turn_led_off(self, serial_mock):
        uut = NanoProcessor()
        uut.ser = serial_mock

        uut.led_off()

        serial_mock.write.assert_called_once_with(LED_OFF)

    @patch('controller.processors.nano_processor.serial')
    def test_should_send_get_distance_request(self, serial_mock):
        uut = NanoProcessor()
        uut.ser = serial_mock

        uut.get_distance_request()

        serial_mock.write.assert_called_once_with('1;'.encode('utf-8'))

    @patch('controller.processors.nano_processor.serial')
    def test_should_read_distance(self, serial_mock):
        expected_result = 11
        serial_mock.readline.return_value = str(expected_result).encode()
        uut = NanoProcessor()
        uut.ser = serial_mock

        result = uut.read_distance()

        serial_mock.readline.assert_called_once()
        self.assertEquals(result, expected_result)

    @patch('controller.processors.nano_processor.serial')
    def test_should_fail_to_read_distance_if_received_wrong_value(self, serial_mock):
        expected_result = 'not_int'
        serial_mock.readline.return_value = str(expected_result).encode()
        uut = NanoProcessor()
        uut.ser = serial_mock

        result = uut.read_distance()

        serial_mock.readline.assert_called_once()
        self.assertEquals(result, 0)

    @patch('controller.processors.nano_processor.serial')
    def test_should_set_pan_position(self, serial_mock):
        pan_position = 123
        uut = NanoProcessor()
        uut.ser = serial_mock

        uut.set_pan_position(pan_position)

        serial_mock.write.assert_called_once_with('2:0:123;'.encode('utf-8'))

    @patch('controller.processors.nano_processor.serial')
    def test_should_set_tilt_position(self, serial_mock):
        tilt_position = 123
        uut = NanoProcessor()
        uut.ser = serial_mock

        uut.set_tilt_position(tilt_position)

        serial_mock.write.assert_called_once_with('2:1:123;'.encode('utf-8'))

    @patch('controller.processors.nano_processor.serial')
    def test_should_send_get_accelerometer_data_request(self, serial_mock):
        uut = NanoProcessor()
        uut.ser = serial_mock

        uut.get_accelerometer_data_request()

        serial_mock.write.assert_called_once_with('3;'.encode('utf-8'))

    @patch('controller.processors.nano_processor.serial')
    def test_should_send_read_accelerometer_data(self, serial_mock):
        expected_result = 'received_data'
        serial_mock.readline.return_value = str(expected_result).encode()
        uut = NanoProcessor()
        uut.ser = serial_mock

        result = uut.read_accelerometer_data()

        serial_mock.readline.assert_called_once_with()
        self.assertEquals(result, expected_result)

    @patch('controller.processors.nano_processor.serial')
    def test_should_send_get_ktir_data_request(self, serial_mock):
        uut = NanoProcessor()
        uut.ser = serial_mock

        uut.get_ktir_data_request()

        serial_mock.write.assert_called_once_with('4;'.encode('utf-8'))

    @patch('controller.processors.nano_processor.serial')
    def test_should_read_ktir_data(self, serial_mock):
        expected_result = 'received_data'
        serial_mock.readline.return_value = str(expected_result).encode()
        uut = NanoProcessor()
        uut.ser = serial_mock

        result = uut.read_ktir_data()

        serial_mock.readline.assert_called_once_with()
        self.assertEquals(result, expected_result)
