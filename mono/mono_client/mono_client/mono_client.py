#!/usr/bin/python3

import json
import logging
import requests


class MonoClient:

    logger = logging.getLogger('Mono client')
    base_url = 'http://localhost:5100/mono'
    nano_url = base_url + '/nano'
    mini_driver_url = base_url + '/mini_driver'
    mini_driver_led_on_url = mini_driver_url + '/led_on'
    mini_driver_led_off_url = mini_driver_url + '/led_off'
    nano_led_on_url = nano_url + '/led_on'
    nano_led_off_url = nano_url + '/led_off'
    pan_url = nano_url + '/pan'
    tilt_url = nano_url + '/tilt'
    ultrasonic_url = nano_url + '/ultrasonic'
    accelerometer_url = nano_url + '/accelerometer'
    ktir_url = nano_url + '/ktir'
    alarm_url = base_url + '/alarm'

    def mini_driver_led_on(self):
        self.logger.info('Mini driver led on')
        requests.get(self.mini_driver_led_on_url, verify=False)

    def mini_driver_led_off(self):
        self.logger.info('Mini driver led off')
        requests.get(self.mini_driver_led_off_url, verify=False)

    def nano_led_on(self):
        self.logger.info('Nano led on')
        requests.get(self.nano_led_on_url, verify=False)

    def nano_led_off(self):
        self.logger.info('Nano led off')
        requests.get(self.nano_led_off_url, verify=False)

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

    def report_alarm(self, alarm):
        data = dict(alarm=alarm)
        r = requests.put(self.alarm_url, params=data, verify=False)
        if r.status_code != requests.codes.ok:
            self.logger.info('Can\'t report alarm. Status ' + str(r.status_code))
            return

        self.logger.info('Report alarm: ' + alarm + '. Status ' + str(r.status_code))

    def remove_alarm(self, alarm):
        data = dict(alarm=alarm)
        r = requests.delete(self.alarm_url, params=data, verify=False)
        if r.status_code != requests.codes.ok:
            self.logger.info('Can\'t remove alarm. Status ' + str(r.status_code))
            return

        self.logger.info('Remove alarm: ' + alarm + '. Status ' + str(r.status_code))