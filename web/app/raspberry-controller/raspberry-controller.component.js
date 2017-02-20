'use strict';

// Register `raspberry-controller` component, along with its associated controller and template
angular.
  module('raspberry').
  component('raspberry', {
    templateUrl: 'raspberry-controller/raspberry-controller.template.html',
    controller: ['$http', '$interval', 'Path', function RaspberryController($http, $interval, Path) {

        this.controllerData = {
            forwardSpeed: 0,
            backSpeed: 0,
            leftOffset: 0,
            rightOffset: 0,
        }
        var self = this
        var maxSpeed = 250
        this.distance = 0
        this.danger = false
        var ledOn = false

        this.getDistance = function() {
            /*$http.get(Path.DISTANCE).then(function(response) {
                var data = response.data;
                self.distance = data.distance
                if (self.distance <= 20) {
                    self.danger = true;
                } else {
                    self.danger = false;
                }
            });*/
        }



        this.blinkLed = function() {
            if (!ledOn) {
                ledOn = true;
                $http.get(Path.LED_ON);
            } else {
                ledOn = false;
                $http.get(Path.LED_OFF);
            }
        }

        this.sendSpeed = function(leftSpeed, rightSpeed) {
            var req = {
                 method: 'GET',
                 url: Path.DRIVE,
                 params: {
                    left: leftSpeed,
                    right: rightSpeed
                 }
            }
            $http(req)
        }

        this.buttonUpDown = function() {
            this.sendSpeed(getLeftSpeed(), getRightSpeed())
        }

        this.buttonLeftDown = function() {
            this.sendSpeed(getLeftSpeed(), 0)
        }

        this.buttonDownDown = function() {
            this.sendSpeed(getBackLeftSpeed(), getBackRightSpeed())
        }

        this.buttonRightDown = function() {
            this.sendSpeed(0, getRightSpeed())
        }

        this.buttonUp = function() {
            this.sendSpeed(0, 0)
        }

        this.getDistancePeriodically = $interval(this.getDistance, 500);

        var getLeftSpeed = function() {
            var leftSpeed = self.controllerData.forwardSpeed + self.controllerData.leftOffset
            if (leftSpeed > maxSpeed) {
                leftSpeed = maxSpeed
            }
            return leftSpeed
        }

        var getRightSpeed = function() {
            var rightSpeed = self.controllerData.forwardSpeed + self.controllerData.rightOffset
            if (rightSpeed > maxSpeed) {
                rightSpeed = maxSpeed
            }
            return rightSpeed
        }

        var getBackLeftSpeed = function() {
            var leftSpeed = - self.controllerData.backSpeed - self.controllerData.leftOffset
            if (leftSpeed < -maxSpeed) {
                leftSpeed = -maxSpeed
            }
            return leftSpeed
        }

        var getBackRightSpeed = function() {
            var rightSpeed = - self.controllerData.backSpeed - self.controllerData.rightOffset
            if (rightSpeed < -maxSpeed) {
                rightSpeed = -maxSpeed
            }
            return rightSpeed
        }

        var getInitialData = function() {
            $http.get(Path.INIT_DATA).then(function(response) {
                self.controllerData = response.data
            });
        }

        getInitialData()
    }]
  });
