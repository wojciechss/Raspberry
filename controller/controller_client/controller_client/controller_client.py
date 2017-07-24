#!/usr/bin/python3

import logging
import requests


class ControllerClient:

    logger = logging.getLogger('Controller client')
    controller_url = 'http://localhost:5002/controller'
    alarm_url = controller_url + '/alarm'

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
