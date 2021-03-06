import json
import falcon
import logging


class NanoApiBase(object):
    def __init__(self, nano):
        self.logger = logging.getLogger('Nano')
        self.logger.setLevel(logging.WARNING)
        self.nano = nano


class LedOn(NanoApiBase):
    def __init__(self, nano):
        super(LedOn, self).__init__(nano)

    def on_get(self, req, resp):
        self.nano.led_on()
        self.logger.info('Led on')
        resp.status = falcon.HTTP_200


class LedOff(NanoApiBase):
    def __init__(self, nano):
        super(LedOff, self).__init__(nano)

    def on_get(self, req, resp):
        self.nano.led_off()
        self.logger.info('Led off')
        resp.status = falcon.HTTP_200


class SetPanPosition(NanoApiBase):
    def __init__(self, nano):
        super(SetPanPosition, self).__init__(nano)

    def on_post(self, req, resp):
        position = req.get_param('position')
        self.logger.info('Pan position: ' + str(position))
        self.nano.set_pan_position(int(position))
        resp.status = falcon.HTTP_200


class SetTiltPosition(NanoApiBase):
    def __init__(self, nano):
        super(SetTiltPosition, self).__init__(nano)

    def on_post(self, req, resp):
        position = req.get_param('position')
        self.logger.info('Tilt position: ' + str(position))
        self.nano.set_tilt_position(int(position))
        resp.status = falcon.HTTP_200


class ReadDistance(NanoApiBase):
    def __init__(self, nano):
        super(ReadDistance, self).__init__(nano)

    def on_get(self, req, resp):
        self.nano.get_distance_request()
        distance = self.nano.read_distance()
        self.logger.info('Distance: ' + str(distance))
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(dict(data=distance))


class ReadAccelerometer(NanoApiBase):
    def __init__(self, nano):
        super(ReadAccelerometer, self).__init__(nano)

    def on_get(self, req, resp):
        self.nano.get_accelerometer_data_request()
        acc_data = self.nano.read_accelerometer_data()
        self.logger.info('Accelerometer: ' + str(acc_data))
        data = dict(data=acc_data)
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(data)


class ReadKtir(NanoApiBase):
    def __init__(self, nano):
        super(ReadKtir, self).__init__(nano)

    def on_get(self, req, resp):
        self.nano.get_ktir_data_request()
        ktir_data = self.nano.read_ktir_data()
        self.logger.info('Ktir: ' + str(ktir_data))
        data = dict(data=ktir_data)
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(data)
