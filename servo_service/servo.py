#!/usr/bin/python3

from servo_pwm import ServoPWM

PAN_PWM_PIN = 23
TILT_PWM_PIN = 24


class Servo:
    def __init__(self):
        self.pan = ServoPWM(PAN_PWM_PIN, (45.0, 1850), (90.0, 1400), (135.0, 1000.0))
        self.tilt = ServoPWM(TILT_PWM_PIN, (45.0, 1850), (90.0, 1400), (135.0, 1000.0))

    def __del__(self):
        ServoPWM.cleanup()

    def set_pan_position(self, position):
        self.pan.set_angle(position)

    def set_tilt_position(self, position):
        self.tilt.set_angle(position)