#!/usr/bin/python3

import RPIO
import RPIO.PWM

PWM_DMA_CHANNEL = 0
PWM_SUBCYLCLE_TIME_US = 20000
PWM_PULSE_INCREMENT_US = 10

ABSOLUTE_MIN_PULSE_WIDTH_US = 500
ABSOLUTE_MAX_PULSE_WIDTH_US = 2500


class ServoPWM:

    def __init__(self, pwm_pin, min_angle_pulse_width_pair,
                 mid_angle_pulse_width_pair, max_angle_pulse_width_pair):

        # Check that the given angles are valid
        assert (min_angle_pulse_width_pair[0] >= 0)
        assert (mid_angle_pulse_width_pair[0] > min_angle_pulse_width_pair[0])
        assert (mid_angle_pulse_width_pair[0] < max_angle_pulse_width_pair[0])
        assert (max_angle_pulse_width_pair[0] <= 180)

        self.pwm_pin = pwm_pin
        self.min_angle_pulse_width_pair = min_angle_pulse_width_pair
        self.mid_angle_pulse_width_pair = mid_angle_pulse_width_pair
        self.max_angle_pulse_width_pair = max_angle_pulse_width_pair
        self.last_pulse_width_set = None

    @staticmethod
    def init_channel():
        # Setup RPIO, and prepare for PWM signals
        RPIO.setmode(RPIO.BCM)

        RPIO.PWM.setup(pulse_incr_us=PWM_PULSE_INCREMENT_US)
        RPIO.PWM.init_channel(PWM_DMA_CHANNEL, PWM_SUBCYLCLE_TIME_US)

    def clear_pwm(self):
        RPIO.PWM.clear_channel_gpio(PWM_DMA_CHANNEL, self.pwm_pin)
        RPIO.PWM.cleanup()

    @staticmethod
    def cleanup():
        RPIO.cleanup()

    def set_pulse_width(self, pulse_width):
        # Constrain the pulse width
        if pulse_width < ABSOLUTE_MIN_PULSE_WIDTH_US:
            pulse_width = ABSOLUTE_MIN_PULSE_WIDTH_US
        if pulse_width > ABSOLUTE_MAX_PULSE_WIDTH_US:
            pulse_width = ABSOLUTE_MAX_PULSE_WIDTH_US

        # Ensure that the pulse width is an integer multiple of the smallest
        # possible pulse increment
        pulse_increment_us = RPIO.PWM.get_pulse_incr_us()
        num_pulses_needed = int(pulse_width / pulse_increment_us)
        pulse_width = num_pulses_needed * pulse_increment_us

        if pulse_width != self.last_pulse_width_set:
            RPIO.PWM.add_channel_pulse(PWM_DMA_CHANNEL, self.pwm_pin, 0, num_pulses_needed)
            self.last_pulse_width_set = pulse_width

    def set_angle(self, angle):
        # Constrain the angle
        if angle < self.min_angle_pulse_width_pair[0]:
            angle = self.min_angle_pulse_width_pair[0]
        if angle > self.max_angle_pulse_width_pair[0]:
            angle = self.max_angle_pulse_width_pair[0]

        # Convert the angle to a pulse width using linear interpolation
        if angle < self.mid_angle_pulse_width_pair[0]:

            angle_diff = self.mid_angle_pulse_width_pair[0] - self.min_angle_pulse_width_pair[0]
            start_pulse_width = self.min_angle_pulse_width_pair[1]
            pulse_width_diff = self.mid_angle_pulse_width_pair[1] - self.min_angle_pulse_width_pair[1]

            interpolation = float(angle - self.min_angle_pulse_width_pair[0]) / angle_diff

            pulse_width = start_pulse_width + interpolation * pulse_width_diff

        else:

            angle_diff = self.max_angle_pulse_width_pair[0] - self.mid_angle_pulse_width_pair[0]
            start_pulse_width = self.mid_angle_pulse_width_pair[1]
            pulse_width_diff = self.max_angle_pulse_width_pair[1] - self.mid_angle_pulse_width_pair[1]

            interpolation = float(angle - self.mid_angle_pulse_width_pair[0]) / angle_diff

            pulse_width = start_pulse_width + interpolation * pulse_width_diff

        # Now set the pulse width
        self.set_pulse_width(pulse_width)
