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

        if (data.angle.degree > 0 && data.angle.degree <= 45) {
            speed.left = acceleration;
            speed.right = 0;
        } else if (data.angle.degree > 45 && data.angle.degree < 135) {
            speed.left = acceleration;
            speed.right = acceleration;
        } else if (data.angle.degree >= 135 && data.angle.degree < 180) {
            speed.left = 0;
            speed.right = acceleration;
        } else if (data.angle.degree >= 180 && data.angle.degree <= 360) {
            speed.left = -100
            speed.right = -100;
        }
        return speed;
    }

    return {
        convertSpeed: _convertSpeed
    }
  });