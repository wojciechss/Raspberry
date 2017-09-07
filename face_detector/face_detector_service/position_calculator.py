#!/usr/bin/python3

from enum import Enum


class PositionCalculator:

    DISTANCE = Enum('DISTANCE', 'CLOSE OK FAR')
    SECTION = Enum('SECTION', 'FIRST CENTER SECOND')

    def __init__(self, section_size):
        self.section_size = section_size

    def distance(self, length, full_length):
        min_length = (full_length - full_length * 0.1) / 2
        max_length = (full_length + full_length * 0.1) / 2
        if length < min_length:
            return self.DISTANCE.FAR
        elif length > max_length:
            return self.DISTANCE.CLOSE
        else:
            return self.DISTANCE.OK

    def section(self, position, length, full_length):
        if (position + length) < 0.5 * full_length:
            first_half = 0
            second_half = 1
        elif position > 0.5 * full_length:
            first_half = 1
            second_half = 0
        else:
            first_half = ((position + length) - 0.5 * full_length) / length
            second_half = 1 - first_half

        if second_half > self.section_size:
            return self.SECTION.FIRST
        elif first_half > self.section_size:
            return self.SECTION.SECOND
        else:
            return self.SECTION.CENTER