#!/usr/bin/python3

import requests


class MiniDriverClient:

    base_url = 'http://localhost:5000/mini_driver'
    drive_url = base_url + '/drive'
    led_on_url = base_url + '/led_on'
    led_off_url = base_url + '/led_off'

    def led_on(self):
        r = requests.get(self.led_on_url, verify=False)
        r.raise_for_status()

    def led_off(self):
        r = requests.get(self.led_off_url, verify=False)
        r.raise_for_status()

    def drive(self, left, right):
        data = dict(left=left, right=right)
        r = requests.post(self.drive_url, params=data, verify=False)
        r.raise_for_status()
