import falcon
import logging

from processors.mini_driver_processor import MiniDriverProcessor


class MiniDriverApiBase(object):
    def __init__(self, mini_driver):
        self.logger = logging.getLogger('Mini driver')
        self.mini_driver = mini_driver


class LedOn(MiniDriverApiBase):
    def __init__(self, mini_driver):
        super(LedOn, self).__init__(mini_driver)

    def on_get(self, req, resp):
        self.mini_driver.led_on()
        self.logger.info('Led on')
        resp.status = falcon.HTTP_200


class LedOff(MiniDriverApiBase):
    def __init__(self, mini_driver):
        super(LedOff, self).__init__(mini_driver)

    def on_get(self, req, resp):
        self.mini_driver.led_off()
        self.logger.info('Led off')
        resp.status = falcon.HTTP_200


class Drive(MiniDriverApiBase):
    def __init__(self, mini_driver):
        super(Drive, self).__init__(mini_driver)

    def on_post(self, req, resp):
        left = req.get_param('left')
        right = req.get_param('right')
        self.mini_driver.drive(left, right)
        self.logger.info('Drive: ' + left + ':' + right)
        resp.status = falcon.HTTP_200


class MiniDriverApiFactory(object):

    @staticmethod
    def create(api):
        mini_driver = MiniDriverProcessor()
        mini_driver.connect()
        api.add_route('/mini_driver/led_on', LedOn(mini_driver))
        api.add_route('/mini_driver/led_off', LedOff(mini_driver))
        api.add_route('/mini_driver/drive', Drive(mini_driver))
