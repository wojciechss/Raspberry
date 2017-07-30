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

    this.setSpeed = function (leftSpeed, rightSpeed) {
        var changed  = false;
        if (Math.abs(lastLeftSpeed - leftSpeed) > 20) {
            lastLeftSpeed = leftSpeed;
            changed = true;
        }
        if (Math.abs(lastRightSpeed - rightSpeed) > 20) {
            lastRightSpeed = rightSpeed;
            changed = true;
        }
        if (changed) {
            this.sendSpeed(Math.floor(leftSpeed), Math.floor(rightSpeed));
        }
    }

    this.convertAndSetSpeed = function (data) {
        var speed = SpeedConverter.convertSpeed(data);
        this.setSpeed(speed.left, speed.right)
    };
  }]);