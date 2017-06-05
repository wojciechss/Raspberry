'use strict';

// Register `raspberry-controller` component, along with its associated controller and template
angular.
  module('raspberry').
  service('Servo', ['$http', 'Path', function($http, Path) {

    this.setServoPosition = function(position) {
        var req = {
             method: 'GET',
             url: Path.SERVO,
             params: {
                position: position,
             }
        }
        $http(req)
    }
  }]);