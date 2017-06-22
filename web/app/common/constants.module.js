'use strict';

angular.
  module('constants', []).
  factory('Path', [function() {
    var mini_driver = '/mini_driver';
    var nano = '/nano';
    return {
        INIT_DATA: mini_driver + '/init_data',
        DRIVE: mini_driver + '/drive',
        DISTANCE: nano + '/ultrasonic',
        MINI_LED_ON: mini_driver + '/led_on',
        MINI_LED_OFF: mini_driver + '/led_off',
        NANO_LED_ON: nano + '/led_on',
        NANO_LED_OFF: nano + '/led_off',
        PAN: nano + '/pan',
        TILT: nano + '/tilt'
    }
}]);