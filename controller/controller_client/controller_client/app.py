#!/usr/bin/python3

import json
from controller_client import ControllerClient


if __name__ == "__main__":
    print('start')
    data = json.dumps({'type': 'face', 'content': [{'vertical': 1, 'horizontal': 1, 'distance': 1}]})
    ControllerClient().report_event(data)
