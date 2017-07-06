#!/usr/bin/python3

import sys
import logging


class AlarmProcessor:

    logger = logging.getLogger('Alarm processor')
    alarms = []

    def add_alarm(self, alarm):
        if self.get_alarm(alarm) > 0:
            self.logger.info('Alarm already reported: ' + alarm)
            return
        self.logger.info('Add alarm: ' + alarm)
        self.alarms.append(alarm)

    def remove_alarm(self, alarm):
        if self.get_alarm(alarm) == 0:
            self.logger.info('Alarm not found: ' + alarm)
            return
        self.logger.info('Remove alarm: ' + alarm)
        self.alarms.remove(alarm)

    def get_alarm(self, alarm):
        count = self.alarms.count(alarm)
        self.logger.info('Alarms: ' + str(count))
        return count
