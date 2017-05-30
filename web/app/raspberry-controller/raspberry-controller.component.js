'use strict';

// Register `raspberry-controller` component, along with its associated controller and template
angular.
  module('raspberry').
  component('raspberry', {
    templateUrl: 'raspberry-controller/raspberry-controller.template.html',
    controller: ['$http', '$interval', 'Path', 'MobileDetector',
            function RaspberryController($http, $interval, Path, MobileDetector) {

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

        var forwardSpeed = 0;
        var sidewaysSpeed = 0;

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

        this.isMobile = function() {
            return MobileDetector.isMobile()
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


        var joystickL = nipplejs.create({
            zone: document.getElementById('left'),
            mode: 'dynamic',
            color: 'black',
            threshold: 0.9,
            size: 100
        });

        joystickL.on('removed', function (evt, nipple) {
            nipple.off('start move end dir plain');
                console.log("off");
        }).on('move', function (evt, data) {
                // DO EVERYTHING
                var x = Math.cos(data.angle.radian) * data.distance * 4;
                var y = Math.sin(data.angle.radian) * data.distance * 4;
                //console.log(x + ' ' + y)
                if (Math.abs(forwardSpeed - x) > 20) {
                    forwardSpeed = x;
                    console.log('x: ' + x);
                }
                if (Math.abs(sidewaysSpeed - y) > 20) {
                    sidewaysSpeed = y;
                    console.log('y: ' + y);
                }

        });

        var joystickR = nipplejs.create({
            zone: document.getElementById('right'),
            mode: 'dynamic',
            color: 'black',
            size: 100
        });

        getInitialData()
    }]
  });
