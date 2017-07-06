#!/usr/bin/python3

import sys
import logging
import requests


class NanoClient:

    logger = logging.getLogger('Nano client')
    nano_url = 'https://localhost/nano'
    led_on_url = nano_url + '/led_on'
    led_off_url = nano_url + '/led_off'

    def led_on(self):
        self.logger.info('Led on')
        requests.get(self.led_on_url, verify=False)

    def led_off(self):
        self.logger.info('Led off')
        requests.get(self.led_off_url, verify=False)
