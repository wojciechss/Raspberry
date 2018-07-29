#!/usr/bin/python3

import sys
import falcon
import logging

from rest.mini_driver_api import MiniDriverApiFactory
from rest.nano_api import NanoApiFactory

logger = logging.getLogger('Mini driver service')
handler = logging.StreamHandler()
handler.setLevel(logging.WARNING)
logger.addHandler(handler)
logger.handlers.extend(logging.getLogger("gunicorn.error").handlers)

logging.basicConfig(stream=sys.stdout,
                    level=logging.DEBUG,
                    format='[%(asctime)s] [%(process)s] [%(levelname)s] [%(name)s] %(message)s')

api = falcon.API()
MiniDriverApiFactory.create(api)
NanoApiFactory.create(api)
