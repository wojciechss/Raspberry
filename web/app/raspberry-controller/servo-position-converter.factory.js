'use strict';

angular.
  module('raspberry').
  factory('ServoPositionConverter', function() {

    var _convertPanPosition = function (data) {
        if (data.direction.y === 'up') {
            return 130;
        } else if (data.direction.y === 'down') {
            return 180;
        }
    }

    var _convertTiltPosition = function (data) {
        if (data.direction.x === 'left') {
            return 120;
        } else if (data.direction.x === 'right') {
            return 60;
        }
    }

    return {
        convertPanPosition: _convertPanPosition,
        convertTiltPosition: _convertTiltPosition
    }
  });