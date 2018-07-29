#!/usr/bin/python3


class PositionConverter:

    @staticmethod
    def convert_face_position(faces):
        result = []
        for (x, y, w, h) in faces:
            result.append([x + int(0.5 * w), y + int(0.5 * h), w])
        return result

    @staticmethod
    def convert_ball_position(balls):
        result = []
        for (x, y, r) in balls:
            result.append([x, y, 2 * int(r)])
        return result
