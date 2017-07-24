#!/usr/bin/python3

import logging
import requests


class MiniDriverClient:

    logger = logging.getLogger('Mini driver client')
    base_url = 'http://localhost:5000/mini_driver'
    drive_url = base_url + '/drive'
    led_on_url = base_url + '/led_on'
    led_off_url = base_url + '/led_off'

    def led_on(self):
        self.logger.info('Led on')
        requests.get(self.led_on_url, verify=False)

    def led_off(self):
        self.logger.info('Led off')
        requests.get(self.led_off_url, verify=False)

    def drive(self, left, right):
        data = dict(left=left, right=right)
        r = requests.post(self.drive_url, params=data, verify=False)
        if r.status_code != requests.codes.ok:
            self.logger.info('Can\'t drive. Status ' + str(r.status_code))
            return

        self.logger.info('Drive: ' + str(left) + ':' + str(right) + '. Status ' + str(r.status_code))
