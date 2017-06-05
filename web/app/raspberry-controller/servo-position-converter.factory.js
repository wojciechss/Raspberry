'use strict';

angular.
  module('raspberry').
  factory('ServoPositionConverter', function() {

    var _convertPosition = function (data) {
        if (data.direction.y === 'up') {
            return 130;
        } else if (data.direction.y === 'down') {
            return 180;
        }
    }

    return {
        convertPosition: _convertPosition
    }
  });