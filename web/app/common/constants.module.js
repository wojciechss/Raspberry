'use strict';

angular.
  module('constants', []).
  factory('Path', [function() {
    var mini_driver = '/mini_driver';
    var servo = '/servo';
    return {
        INIT_DATA: mini_driver + '/init_data',
        DRIVE: mini_driver + '/drive',
        DISTANCE: mini_driver + '/ultrasonic',
        LED_ON: mini_driver + '/led_on',
        LED_OFF: mini_driver + '/led_off',
        SERVO: controller + '/pan'
    }
}]);