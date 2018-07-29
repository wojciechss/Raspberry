#!/usr/bin/python3

import requests


class ControllerClient:

    controller_url = 'http://localhost:5002/controller'
    alarm_url = controller_url + '/alarm'
    event_url = controller_url + '/event'

    def report_alarm(self, alarm):
        data = dict(alarm=alarm)
        r = requests.put(self.alarm_url, params=data, verify=False)
        r.raise_for_status()

    def remove_alarm(self, alarm):
        data = dict(alarm=alarm)
        r = requests.delete(self.alarm_url, params=data, verify=False)
        r.raise_for_status()

    def report_event(self, data):
        headers = {'Content-type': 'application/json'}
        r = requests.put(self.event_url, data=data, headers=headers)
        r.raise_for_status()
