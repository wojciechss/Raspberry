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

                self.logger.info(horizontal + ':' + vertical + ':' + distance)
