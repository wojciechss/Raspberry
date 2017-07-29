#!/usr/bin/python3

import json
import requests


class NanoClient:

    base_url = 'http://localhost:5001/nano'
    led_on_url = base_url + '/led_on'
    led_off_url = base_url + '/led_off'
    pan_url = base_url + '/pan'
    tilt_url = base_url + '/tilt'
    ultrasonic_url = base_url + '/ultrasonic'
    accelerometer_url = base_url + '/accelerometer'
    ktir_url = base_url + '/ktir'

    def led_on(self):
        r = requests.get(self.led_on_url, verify=False)
        r.raise_for_status()

    def led_off(self):
        r = requests.get(self.led_off_url, verify=False)
        r.raise_for_status()

    def set_pan_position(self, position):
        data = dict(position=position)
        r = requests.post(self.pan_url, params=data, verify=False)
        r.raise_for_status()

    def set_tilt_position(self, position):
        data = dict(position=position)
        r = requests.post(self.tilt_url, params=data, verify=False)
        r.raise_for_status()

    def read_distance(self):
        r = requests.get(self.ultrasonic_url, verify=False)
        r.raise_for_status()
        return json.loads(r.content.decode('utf-8'))['data']

    def read_accelerometer(self):
        r = requests.get(self.accelerometer_url, verify=False)
        r.raise_for_status()
        return json.loads(r.content.decode('utf-8'))['data']

    def read_ktir(self):
        r = requests.get(self.ktir_url, verify=False)
        r.raise_for_status()
        return json.loads(r.content.decode('utf-8'))['data']
