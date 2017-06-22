'use strict';

// Register `raspberry-controller` component, along with its associated controller and template
angular.
  module('raspberry').
  service('Servo', ['$http', 'Path', function($http, Path) {

    this.setPanPosition = function(position) {
        var req = {
             method: 'GET',
             url: Path.PAN,
             params: {
                position: position,
             }
        }
        $http(req)
    }

    this.setTiltPosition = function(position) {
        var req = {
             method: 'GET',
             url: Path.TILT,
             params: {
                position: position,
             }
        }
        $http(req)
    }
  }]);