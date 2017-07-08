#!/usr/bin/python3

import json
import logging
import requests


class NanoClient:

    logger = logging.getLogger('Nano client')
    base_url = 'https://localhost/nano'
    ultrasonic_url = base_url + '/ultrasonic'

    def get_distance(self):
        r = requests.get(self.ultrasonic_url, verify=False)
        if r.status_code != requests.codes.ok:
            self.logger.info('Can\'t read distance. Status ' + str(r.status_code))
            return None

        distance = json.loads(r.content.decode('utf-8'))['distance']
        self.logger.info('Distance: ' + str(distance))
        return distance
