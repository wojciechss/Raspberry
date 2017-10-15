#!/usr/bin/python3

import math


class SectionCalculator:

    @staticmethod
    def calculate(sections, x, y, w, h):
        section_x = math.ceil(x / (w / sections))
        section_y = math.ceil(y / (h / sections))
        return SectionCalculator._check_section(section_x), \
            SectionCalculator._check_section(section_y)

    @staticmethod
    def _check_section(section):
        return section if section > 0 else 1