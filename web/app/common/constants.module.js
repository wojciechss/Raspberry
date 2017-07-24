'use strict';

angular.
  module('constants', []).
  factory('Path', [function() {
    var mini = '/mini_driver';
    var nano = '/nano';
    return {
        DRIVE: mini + '/drive',
        PAN: nano + '/pan',
        TILT: nano + '/tilt'
    }
}]);