'use strict';

// Register `phoneList` component, along with its associated controller and template
angular.
  module('raspberry').
  component('raspberry', {
    templateUrl: 'raspberry/raspberry.template.html',
    controller: function RaspberryController($http) {

        var ledOn = false;
        this.ledStatus = 'led on';

        this.blinkLed = function() {
            if (ledOn) {
                ledOn = false;
                $http.get('/led_on');
                this.ledStatus = 'led on';
            } else {
                ledOn = true;
                $http.get('/led_off');
                this.ledStatus = 'led off';
            }
        }

    }
  });
