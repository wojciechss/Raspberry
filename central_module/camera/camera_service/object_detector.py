#!/usr/bin/python3

import cv2
from face_detector import FaceDetector
from ball_detector import BallDetector
from stream_reader import StreamReader
from position_converter import PositionConverter
from section_calculator import SectionCalculator


class ObjectDetector:

    stream_url = 'http://samantha:8081/?action=stream'

    def __init__(self):
        self.stream_reader = StreamReader(self.stream_url)
        self.face_detector = FaceDetector()
        self.ball_detector = BallDetector()
        self.position_converter = PositionConverter()
        self.sections = 5
        self.face_type = 'face'
        self.ball_type = 'ball'

    def detect(self, object_name):
        img = self.stream_reader.read()
        objects = []

        if object_name == self.face_type:
            faces = self.detect_faces(img)
            objects.append(faces)

        if object_name == self.ball_type:
            balls = self.detect_balls(img)
            objects.append(balls)

        return dict(objects=objects)

    def detect_faces(self, img):
        height = img.shape[0]
        width = img.shape[1]
        faces = self.face_detector.detect(img)
        positions = self.position_converter.convert_face_position(faces)
        sections = []
        for position in positions:
            section = SectionCalculator.calculate(
                self.sections, position[0], position[1], width, height)
            sections.append(dict(section_x=section[0], section_y=section[1], size=position[2]))

        return dict(type=self.face_type, content=sections)

    def detect_balls(self, img):
        height = img.shape[0]
        width = img.shape[1]
        balls = self.ball_detector.detect(img)
        positions = self.position_converter.convert_ball_position(balls)
        sections = []
        for position in positions:
            section = SectionCalculator.calculate(
                self.sections, position[0], position[1], width, height)
            sections.append(dict(section_x=section[0], section_y=section[1], size=position[2]))

        return dict(type=self.ball_type, content=sections)
