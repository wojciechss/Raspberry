'use strict';

angular.
  module('constants', []).
  factory('Path', [function() {
    var controller = '/controller';
    var nano = '/nano';
    return {
        DRIVE: controller + '/drive',
        PAN: nano + '/pan',
        TILT: nano + '/tilt'
    }
}]);