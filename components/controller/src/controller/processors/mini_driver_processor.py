import time
import serial


# Input:       'device:device_specific_data;'
# Led:         '0:{state};' on - 1, off - 0
# Motor:       '1:{left_speed}:{right_speed};'
class MiniDriverProcessor:

    portName = '/dev/miniDriver'

    def __init__(self):
        self.ser = serial.Serial(
            port=self.portName,
            baudrate=9600,
            timeout=5
        )

    def connect(self):
        self._blink_led()

    def led_on(self):
        self._write('0:1;')

    def led_off(self):
        self._write('0:0;')

    def drive(self, left_speed, right_speed):
        data = '1:{}:{};'.format(str(left_speed), str(right_speed))
        self._write(data)

    def _write(self, data):
        self.ser.write(data.encode('utf-8'))

    def _read_line(self):
        return self.ser.readline()

    def _blink_led(self):
        self.led_on()
        time.sleep(0.5)
        self.led_off()
        time.sleep(0.5)
        self.led_on()
        time.sleep(0.5)
        self.led_off()
