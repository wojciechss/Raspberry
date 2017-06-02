'use strict';

angular.
  module('raspberry').
  factory('SpeedConverter', function() {

    var _convertSpeed = function (data) {
        var acceleration = data.distance * 4;
        var x = Math.cos(data.angle.radian) * acceleration;
        var y = Math.sin(data.angle.radian) * acceleration;
        var speed = {
            left: 0,
            right: 0,
        }

        if (data.angle.degree > 0 && data.angle.degree <= 90) {
            speed.left = acceleration;
            speed.right = acceleration - x;
            if (speed.right < 0) {
                speed.right = 0;
            }
        } else if (data.angle.degree > 90 && data.angle.degree <= 180) {
            speed.left = acceleration + x;
            if (speed.left < 0) {
                speed.left = 0;
            }
            speed.right = acceleration;
        } else if (data.angle.degree > 180 && data.angle.degree <= 270) {
            speed.left = (-acceleration - x) / 2;
            if (speed.left > 0) {
                speed.left = 0;
            }
            speed.right = (-acceleration) / 2;
        } else if (data.angle.degree > 270 && data.angle.degree <= 360) {
            speed.left = (-acceleration) / 2;
            speed.right = (-acceleration + x) / 2;
            if (speed.right > 0) {
                speed.right = 0;
            }
        }
        return speed;
    }

    return {
        convertSpeed: _convertSpeed
    }
  });