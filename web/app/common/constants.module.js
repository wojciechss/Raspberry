'use strict';

angular.
  module('constants', []).
  factory('Path', [function() {
    var base_path = '/mono';
    var mini = base_path + '/mini_driver';
    var nano = base_path + '/nano';
    return {
        DRIVE: mini + '/drive',
        PAN: nano + '/pan',
        TILT: nano + '/tilt'
    }
}]);