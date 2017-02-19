'use strict';

angular.
  module('constants', []).
  factory('Path', [function() {
    var controller = '/controller';
    return {
        INIT_DATA: controller + '/init_data',
        DRIVE: controller + '/drive',
        DISTANCE: controller + '/ultrasonic',
        LED_ON: controller + '/led_on',
        LED_OFF: controller + '/led_off'
    }
}]);