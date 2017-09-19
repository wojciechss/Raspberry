#!/usr/bin/python3


import sys
import logging
from face_detector import FaceDetector


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout,
                        level=logging.DEBUG,
                        format='[%(asctime)s] [%(process)s] [%(levelname)s] [%(name)s] %(message)s')
    FaceDetector().run()
