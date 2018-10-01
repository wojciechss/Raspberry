import time
import logging
from controller.processors.nano_processor import NanoProcessor
from controller.processors.mini_driver_processor import MiniDriverProcessor
from controller.rest import nano_api, mini_driver_api


class Runner(object):

    def __init__(self, api):
        self.api = api
        self.logger = logging.getLogger('Api factory')

    def run(self):
        nano = NanoProcessor()
        mini_driver = MiniDriverProcessor()
        self._create_nano(nano)
        self._create_mini(mini_driver)
        self._wait_for_connection()
        nano.connect()
        mini_driver.connect()

    def _create_nano(self, nano):
        self.api.add_route('/nano/led_on', nano_api.LedOn(nano))
        self.api.add_route('/nano/led_off', nano_api.LedOff(nano))
        self.api.add_route('/nano/pan', nano_api.SetPanPosition(nano))
        self.api.add_route('/nano/tilt', nano_api.SetTiltPosition(nano))
        self.api.add_route('/nano/ultrasonic', nano_api.ReadDistance(nano))
        self.api.add_route('/nano/accelerometer', nano_api.ReadAccelerometer(nano))
        self.api.add_route('/nano/ktir', nano_api.ReadKtir(nano))

    def _create_mini(self, mini_driver):
        self.api.add_route('/mini_driver/led_on', mini_driver_api.LedOn(mini_driver))
        self.api.add_route('/mini_driver/led_off', mini_driver_api.LedOff(mini_driver))
        self.api.add_route('/mini_driver/drive', mini_driver_api.Drive(mini_driver))

    def _wait_for_connection(self):
        self.logger.info('Waiting')
        for i in range(0, 10):
            time.sleep(1)
        self.logger.info('Connected')
