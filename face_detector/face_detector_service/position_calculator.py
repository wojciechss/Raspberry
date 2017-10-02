#!/usr/bin/python3


class PositionCalculator:

    def __init__(self, section_size):
        self.section_size = section_size

    def distance(self, length, full_length):
        min_length = (full_length - full_length * 0.1) / 2
        max_length = (full_length + full_length * 0.1) / 2
        if length < min_length:
            return 3
        elif length > max_length:
            return 1
        else:
            return 2

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
            return 1
        elif first_half > self.section_size:
            return 3
        else:
            return 2