#!/usr/bin/python3

import logging
import time

from controller_client.controller_client import ControllerClient
from nano_client.nano_client import NanoClient

DISTANCE = 'DISTANCE'
CRITICAL_DISTANCE = 20

class ObstacleDetector:
    logger = logging.getLogger('Obstacle detector')
    nano_client = NanoClient()
    controller_client = ControllerClient()

    alarm_reported = False

    def run(self):
        self.logger.info('Started analyzing data')
        while (True):
            self.logger.info('Read data')
            time.sleep(0.2)
            distance = self.nano_client.read_distance()
            if distance is not None and distance > 0 and distance < CRITICAL_DISTANCE and not self.alarm_reported:
                self.controller_client.report_alarm(DISTANCE)
                self.alarm_reported = True
            elif distance is not None and distance >= CRITICAL_DISTANCE and self.alarm_reported:
                self.controller_client.remove_alarm(DISTANCE)
                self.alarm_reported = False