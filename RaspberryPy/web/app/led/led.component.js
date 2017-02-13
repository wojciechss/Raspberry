'use strict';

// Register `phoneList` component, along with its associated controller and template
angular.
  module('led').
  component('led', {
    templateUrl: 'led/led.template.html',
    controller: ['$http', '$interval', function LedController($http, $interval) {

        var ledOn = false;
        this.ledStatus = 'led on';

        var self = this;
        this.blinkLed = function() {
            if (ledOn) {
                ledOn = false;
                this.ledStatus = 'led on';
            } else {
                ledOn = true;
                this.ledStatus = 'led off';
            }
        }
    }]
  });
