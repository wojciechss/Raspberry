#!/usr/bin/python3

import sys
import falcon
import logging

from rest_falcon.api_factory import ApiFactory

logger = logging.getLogger('Mini driver service')
handler = logging.StreamHandler()
handler.setLevel(logging.WARNING)
logger.addHandler(handler)
logger.handlers.extend(logging.getLogger("gunicorn.error").handlers)

logging.basicConfig(stream=sys.stdout,
                    level=logging.DEBUG,
                    format='[%(asctime)s] [%(process)s] [%(levelname)s] [%(name)s] %(message)s')

api = falcon.API()
ApiFactory().create(api)
