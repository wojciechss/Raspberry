import time
import logging
from processors.nano_processor import NanoProcessor
from processors.mini_driver_processor import MiniDriverProcessor
from rest import nano_api, mini_driver_api


class ApiFactory(object):

    def __init__(self):
        self.logger = logging.getLogger('Api factory')

    def create(self, api):
        ApiFactory._create_mini(api)
        ApiFactory._create_nano(api)
        self._wait_for_connection()

    @staticmethod
    def _create_nano(api):
        nano = NanoProcessor()
        nano.connect()
        api.add_route('/nano/led_on', nano_api.LedOn(nano))
        api.add_route('/nano/led_off', nano_api.LedOff(nano))
        api.add_route('/nano/pan', nano_api.SetPanPosition(nano))
        api.add_route('/nano/tilt', nano_api.SetTiltPosition(nano))
        api.add_route('/nano/ultrasonic', nano_api.ReadDistance(nano))
        api.add_route('/nano/accelerometer', nano_api.ReadAccelerometer(nano))
        api.add_route('/nano/ktir', nano_api.ReadKtir(nano))

    @staticmethod
    def _create_mini(api):
        mini_driver = MiniDriverProcessor()
        mini_driver.connect()
        api.add_route('/mini_driver/led_on', mini_driver_api.LedOn(mini_driver))
        api.add_route('/mini_driver/led_off', mini_driver_api.LedOff(mini_driver))
        api.add_route('/mini_driver/drive', mini_driver_api.Drive(mini_driver))

    def _wait_for_connection(self):
        self.logger.info('Waiting')
        time.sleep(10)
        self.logger.info('Connected')
