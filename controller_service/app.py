#!/usr/bin/python3

import sys
import json
import falcon
import logging
from alarm_processor import AlarmProcessor
from nano_client import NanoClient

logger = logging.getLogger('Controller service')
handler = logging.StreamHandler()
handler.setLevel(logging.WARNING)
logger.addHandler(handler)
logger.handlers.extend(logging.getLogger("gunicorn.error").handlers)


#logging.basicConfig(stream=sys.stdout,
#                    level=logging.DEBUG,
#                    format='[%(asctime)s] [%(process)s] [%(levelname)s] %(message)s')

api = falcon.API()
alarm_processor = AlarmProcessor()
nano_cli = NanoClient()


class Alarm(object):
    def on_put(self, req, resp):
        alarm = req.get_param('alarm')
        logger.info('Alarm reported: ' + alarm)
        alarm_processor.add_alarm(alarm)
        nano_cli.led_on()

    def on_delete(self, req, resp):
        alarm = req.get_param('alarm')
        logger.info('Alarm removed: ' + alarm)
        alarm_processor.remove_alarm(alarm)
        nano_cli.led_off()

    def on_get(self, req, resp):
        alarm = req.get_param('alarm')
        alarms = alarm_processor.get_alarm(alarm)
        data = dict(alarms=alarms)
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(data)


api.add_route('/controller/alarm', Alarm())
