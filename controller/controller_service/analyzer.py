#!/usr/bin/python3

import time
from threading import Thread

from face_detector_client.face_detector_client import FaceDetectorClient
from event_analyzer import EventAnalyzer

class Analyzer(Thread):
    face_detector_client = FaceDetectorClient()
    event_analyzer = EventAnalyzer()
    running = False

    def stop(self):
        self.running = False

    def start(self):
        self.running = True

    def _run(self):
        while True:
            if self.running:
                print('run')
                data = self.face_detector_client.detect()

                start = time.time()
                print(self.event_analyzer.analyze(data))
                end = time.time()
                duration = end - start
                print("{:.8f}".format(duration))
            time.sleep(1)

    def run(self):
        t1 = Thread(target=self._run)
        t1.setDaemon(True)
        t1.start()

