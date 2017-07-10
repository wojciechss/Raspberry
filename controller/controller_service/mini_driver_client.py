#!/usr/bin/python3

import logging
import requests


class MiniDriverClient:

    logger = logging.getLogger('Mini driver client')
    base_url = 'https://localhost/mini_driver'
    drive_url = base_url + '/drive'

    def drive(self, left, right):
        self.logger.info('Drive')
        data = dict(left=left, right=right)
        r = requests.post(self.drive_url, params=data, verify=False)
        if r.status_code != requests.codes.ok:
            self.logger.info('Can\'t drive. Status ' + str(r.status_code))
            return

        self.logger.info('Drive: ' + left + ':' + right + '. Status ' + str(r.status_code))
