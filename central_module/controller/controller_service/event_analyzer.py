#!/usr/bin/python3

import logging

class EventAnalyzer:

    logger = logging.getLogger('Event analyzer')

    def analyze(self, data):
        if data['type'] == 'face':
            content = data['content']
            if len(content) > 1:
                self.logger.info(data['content'])
            elif len(content) == 1:
                section = content[0]
                horizontal = ''
                if section['horizontal'] == 1:
                    horizontal = 'LEFT'
                elif section['horizontal'] == 2:
                    horizontal = 'CENTER'
                elif section['horizontal'] == 3:
                    horizontal = 'RIGHT'

                vertical = ''
                if section['vertical'] == 1:
                    vertical = 'UP'
                elif section['vertical'] == 2:
                    vertical = 'CENTER'
                elif section['vertical'] == 3:
                    vertical = 'DOWN'

                distance = ''
                if section['distance'] == 1:
                    distance = 'CLOSE'
                elif section['distance'] == 2:
                    distance = 'OK'
                elif section['distance'] == 3:
                    distance = 'FAR'

                result = horizontal + ':' + vertical + ':' + distance
                return result
            return ''

    @staticmethod
    def is_object_detected(data, object_name):
        if data['type'] == object_name:
            content = data['content']
            if len(content) > 0:
                return True
        return False

    def get_section(self, data, object_name):
        if data['type'] == object_name:
            content = data['content']
            if len(content) > 1:
                self.logger.info(data['content'])
            elif len(content) == 1:
                return content[0]
        return None

    def get_horizontal(self, data, object_name):
        section = self.get_section(data, object_name)
        if section is not None:
            return section['section_x']
        return 0

    def get_vertical(self, data, object_name):
        section = self.get_section(data, object_name)
        if section is not None:
            return section['section_y']
        return 0

    def get_size(self, data, object_name):
        section = self.get_section(data, object_name)
        if section is not None:
            return section['size']
        return 0
