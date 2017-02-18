'use strict';

// Register `raspberry-controller` component, along with its associated controller and template
angular.
  module('raspberry').
  component('raspberry', {
    templateUrl: 'raspberry-controller/raspberry-controller.template.html',
    controller: ['$http', '$interval', function RaspberryController($http, $interval) {

        var ledOn = false;
        var self = this;
        this.distance = 0
        this.ledStatus = 'led off';
        this.status = 'Stop';
        this.danger = false;

        this.leftSpeedOffset = 10;
        this.rightSpeedOffset = 10;
        this.baseSpeed = 100;

        this.touched = false;

        this.blinkLed = function() {
            if (!ledOn) {
                ledOn = true;
                $http.get('/controller/led_on');
                this.ledStatus = 'led on';
            } else {
                ledOn = false;
                $http.get('/controller/led_off');
                this.ledStatus = 'led off';
            }
        }

        this.getDistance = function() {
            $http.get('/controller/ultrasonic').then(function(response) {
                var data = response.data;
                self.distance = data.distance
                if (self.distance <= 20) {
                    self.danger = true;
                } else {
                    self.danger = false;
                }
            });
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
            var leftSpeed = this.baseSpeed + this.leftSpeedOffset
            var rightSpeed = this.baseSpeed + this.rightSpeedOffset
            if (leftSpeed > 250) {
                leftSpeed = 250
            }
            if (rightSpeed > 250) {
                rightSpeed = 250
            }
            this.sendSpeed(leftSpeed, rightSpeed)
        }

        this.buttonLeftDown = function() {
            this.status = "LeftDown"
            var leftSpeed = 0
            var rightSpeed = this.baseSpeed + this.rightSpeedOffset
            if (rightSpeed > 250) {
                rightSpeed = 250
            }
            this.sendSpeed(leftSpeed, rightSpeed)
        }

        this.buttonDownDown = function() {
            this.status = "DownDown"
            var leftSpeed = -this.baseSpeed - this.leftSpeedOffset
            var rightSpeed = -this.baseSpeed - this.rightSpeedOffset
            if (leftSpeed < -250) {
                leftSpeed = -250
            }
            if (rightSpeed < -250) {
                rightSpeed = -250
            }
            this.sendSpeed(leftSpeed, rightSpeed)
        }

        this.buttonRightDown = function() {
            this.status = "RightDown"
            var leftSpeed = this.baseSpeed + this.leftSpeedOffset
            var rightSpeed = 0
            if (leftSpeed > 250) {
                leftSpeed = 250
            }
            this.sendSpeed(leftSpeed, rightSpeed)
        }

        this.buttonUp = function() {
            this.status = "Stop"
            this.sendSpeed(0, 0)
        }

        this.getDistancePeriodically = $interval(this.getDistance, 500);
    }]
  });
