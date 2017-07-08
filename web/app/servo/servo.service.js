'use strict';

// Register `raspberry-controller` component, along with its associated controller and template
angular.
  module('raspberry').
  service('Servo', ['$http', 'Path', function($http, Path) {

    var lastTiltPosition = 0;
    var lastPanPosition = 0;

    this.sendPanPosition = function(position) {
        var req = {
             method: 'POST',
             url: Path.PAN,
             params: {
                position: position,
             }
        }
        $http(req)
    }

    this.sendTiltPosition = function(position) {
        var req = {
             method: 'POST',
             url: Path.TILT,
             params: {
                position: position,
             }
        }
        $http(req)
    }

    this.setPanPosition = function (position) {
        if (lastPanPosition != position) {
            lastPanPosition = position;
            this.sendPanPosition(position);
        }
    }

    this.setTiltPosition = function(position) {
        if (lastTiltPosition != position) {
            lastTiltPosition = position;
            this.sendTiltPosition(position);
        }
    }
  }]);