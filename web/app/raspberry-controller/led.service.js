'use strict';

// Register `raspberry-controller` component, along with its associated controller and template
angular.
  module('raspberry').
  service('Led', ['$http', 'Path', function($http, Path) {

        this.ledOn = function() {
            $http.get(Path.LED_ON);
        }

        this.ledOff = function() {
            $http.get(Path.LED_OFF);
        }
  });