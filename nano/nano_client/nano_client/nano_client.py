#!/usr/bin/python3

import json
import logging
import requests


class NanoClient:

    logger = logging.getLogger('Nano client')
    base_url = 'http://localhost:5001/nano'
    led_on_url = base_url + '/led_on'
    led_off_url = base_url + '/led_off'
    pan_url = base_url + '/pan'
    tilt_url = base_url + '/tilt'
    ultrasonic_url = base_url + '/ultrasonic'
    accelerometer_url = base_url + '/accelerometer'
    ktir_url = base_url + '/ktir'

    def led_on(self):
        self.logger.info('Led on')
        requests.get(self.led_on_url, verify=False)

    def led_off(self):
        self.logger.info('Led off')
        requests.get(self.led_off_url, verify=False)

    def set_pan_position(self, position):
        data = dict(position=position)
        r = requests.post(self.pan_url, params=data, verify=False)
        if r.status_code != requests.codes.ok:
            self.logger.info('Can\'t set pan position. Status ' + str(r.status_code))
            return None

        self.logger.info('Set pan position: ' + str(position))

    def set_tilt_position(self, position):
        data = dict(position=position)
        r = requests.post(self.tilt_url, params=data, verify=False)
        if r.status_code != requests.codes.ok:
            self.logger.info('Can\'t set tilt position. Status ' + str(r.status_code))
            return None

        self.logger.info('Set tilt position: ' + str(position))

    def read_distance(self):
        r = requests.get(self.ultrasonic_url, verify=False)
        if r.status_code != requests.codes.ok:
            self.logger.info('Can\'t read distance. Status ' + str(r.status_code))
            return None

        distance = json.loads(r.content.decode('utf-8'))['data']
        self.logger.info('Distance: ' + str(distance))
        return distance

    def read_accelerometer(self):
        r = requests.get(self.accelerometer_url, verify=False)
        if r.status_code != requests.codes.ok:
            self.logger.info('Can\'t read accelerometer. Status ' + str(r.status_code))
            return None

        data = json.loads(r.content.decode('utf-8'))['data']
        self.logger.info('Accelerometer: ' + str(data))
        return data

    def read_ktir(self):
        r = requests.get(self.ktir_url, verify=False)
        if r.status_code != requests.codes.ok:
            self.logger.info('Can\'t read ktir. Status ' + str(r.status_code))
            return None

        data = json.loads(r.content.decode('utf-8'))['data']
        self.logger.info('Ktir: ' + str(data))
        return data
