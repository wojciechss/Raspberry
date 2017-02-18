'use strict';

// Register `raspberry-controller` component, along with its associated controller and template
angular.
  module('raspberry').
  component('raspberry', {
    templateUrl: 'raspberry-controller/raspberry-controller.template.html',
    controller: ['$http', '$interval', function RaspberryController($http, $interval) {

        var ledOn = false;
        var self = this;
        this.distance = 230
        this.ledStatus = 'led on';
        this.status = 'Stop';
        this.danger = false;

        this.leftSpeedOffset = 10;
        this.rightSpeedOffset = 10;

        this.touched = false;

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

        this.sendSpeed = function(leftSpeed, rightSpeed) {
            var req = {
                 method: 'GET',
                 url: '/controller/drive',
                 params: {
                    left: leftSpeed,
                    right: rightSpeed
                 }
            }
            $http(req)
        }

        this.buttonUpDown = function() {
            this.status = "UpDown"
            if (!this.touched) {
                this.touched = true;
                console.log("UpDown")
                var leftSpeed = 100 + this.leftSpeedOffset
                var rightSpeed = 100 + this.rightSpeedOffset
                this.sendSpeed(leftSpeed, rightSpeed)
            }
        }

        this.buttonLeftDown = function() {
            if (!this.touched) {
                this.touched = true;
                this.status = "LeftDown"
                console.log("LeftDown")
                var leftSpeed = 0
                var rightSpeed = 100 + this.rightSpeedOffset
                this.sendSpeed(leftSpeed, rightSpeed)
            }
        }

        this.buttonDownDown = function() {
            if (!this.touched) {
                this.touched = true;
                this.status = "DownDown"
                console.log("DownDown")
                var leftSpeed = -100 - this.leftSpeedOffset
                var rightSpeed = -100 - this.rightSpeedOffset
                this.sendSpeed(leftSpeed, rightSpeed)

            }
        }

        this.buttonRightDown = function() {
            if (!this.touched) {
                this.touched = true;
                this.status = "RightDown"
                console.log("RightDown")
                var leftSpeed = 100 + this.leftSpeedOffset
                var rightSpeed = 0
                this.sendSpeed(leftSpeed, rightSpeed)
            }
        }

        this.buttonUp = function() {
            if (this.touched) {
                this.touched = false;
                this.status = "Stop"
                console.log("Stop")
                this.sendSpeed(0, 0)
            }
        }

        this.getDistancePeriodically = $interval(this.getDistance, 500);
    }]
  });
