#!/usr/bin/python3

import time
from threading import Thread

from camera_client.camera_client import CameraClient
from nano_client.nano_client import NanoClient
from event_analyzer import EventAnalyzer

class Analyzer(Thread):

    def __init__(self):
        self.nano_client = NanoClient()
        self.camera_client = CameraClient()
        self.running = False
        self.ball_type = 'ball'
        self.event_analyzer = EventAnalyzer()

    tilt_position = 85

    def stop(self):
        self.running = False

    def start(self):
        self.running = True
        self.nano_client.set_tilt_position(self.tilt_position)

    def _run(self):
        while True:
            if self.running:
                #start = time.time()
                distance = self.nano_client.read_distance()
                #end = time.time()
                #duration = end - start
                #print("{:.8f}".format(duration))
                #print(str(distance))
                if distance < 80 and distance >= 20:
                    data = self.camera_client.detect(self.ball_type)
                    objects = data['objects']
                    if len(objects) == 1 and self.event_analyzer.is_object_detected(objects[0], self.ball_type):
                        self.adjust_horizontal(objects[0])
                    #if self.event_analyzer.is_face_detected(data):
                        #print('FACE:' + str(distance) + ':' + self.event_analyzer.analyze(data))
                    #    self.adjust_horizontal(data)

                #time.sleep(0.2)
            else:
                time.sleep(1)

    def adjust_horizontal(self, data):
        # 'content': [{'section_y': 3, 'size': 50, 'section_x': 5}]}]}
        horizontal = self.event_analyzer.get_horizontal(data, self.ball_type)
        if horizontal > 0:
            if horizontal == 5:
                if self.tilt_position > 55:
                    self.tilt_position -= 5
                    self.nano_client.set_tilt_position(self.tilt_position)
            elif horizontal == 4:
                if self.tilt_position > 55:
                    self.tilt_position -= 5
                    self.nano_client.set_tilt_position(self.tilt_position)
            elif horizontal == 2:
                if self.tilt_position < 115:
                    self.tilt_position += 5
                    self.nano_client.set_tilt_position(self.tilt_position)
            elif horizontal == 1:
                if self.tilt_position < 115:
                    self.tilt_position += 5
                    self.nano_client.set_tilt_position(self.tilt_position)
            time.sleep(0.2)
            print('pos: ' + str(self.tilt_position) + ' ' + str(horizontal))

    def run(self):
        t1 = Thread(target=self._run)
        t1.setDaemon(True)
        t1.start()

