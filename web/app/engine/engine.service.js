'use strict';

// Register `raspberry-controller` component, along with its associated controller and template
angular.
  module('raspberry').
  service('Engine', ['$http', 'Path', 'SpeedConverter', function($http, Path, SpeedConverter) {

    var self = this;
    var lastLeftSpeed = 0;
    var lastRightSpeed = 0;

    this.sendSpeed = function(leftSpeed, rightSpeed) {
        var req = {
             method: 'POST',
             url: Path.DRIVE,
             params: {
                left: leftSpeed,
                right: rightSpeed
             }
        }
        $http(req)
    }

    this.setSpeed = function (data) {
        var speed = SpeedConverter.convertSpeed(data);
        var changed  = false;
        if (Math.abs(lastLeftSpeed - speed.left) > 20) {
            lastLeftSpeed = speed.left;
            changed = true;
        }
        if (Math.abs(lastRightSpeed - speed.right) > 20) {
            lastRightSpeed = speed.right;
            changed = true;
        }
        if (changed) {
            this.sendSpeed(Math.floor(speed.left), Math.floor(speed.right));
        }
    };
  }]);