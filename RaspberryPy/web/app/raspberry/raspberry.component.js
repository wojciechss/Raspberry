'use strict';

// Register `phoneList` component, along with its associated controller and template
angular.
  module('raspberry').
  component('raspberry', {
    templateUrl: 'raspberry/raspberry.template.html',
    controller: ['$http', '$interval', function RaspberryController($http, $interval) {

        var ledOn = false;
        this.distance = 0
        this.ledStatus = 'led on';

        var self = this;
        this.blinkLed = function() {
            if (ledOn) {
                ledOn = false;
                //$http.get('/controller/led_on');
                this.ledStatus = 'led on';
            } else {
                ledOn = true;
                //$http.get('/controller/led_off');
                this.ledStatus = 'led off';
            }
        }

        this.getDistance = function() {
            //$http.get('/controller/ultrasonic').then(function(response) {
            //    var data = response.data;
            //    self.distance = data.distance
            //});
        }

        this.getDistancePeriodically = $interval(this.getDistance, 500);
    }]
  });
