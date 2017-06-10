'use strict';

// Register `raspberry-controller` component, along with its associated controller and template
angular.
  module('raspberry').
  component('raspberry', {
    templateUrl: 'raspberry-controller/raspberry-controller.template.html',
    controller: ['Engine', 'SpeedConverter', 'Servo', 'ServoPositionConverter', 'MobileDetector',
        function RaspberryController(Engine, SpeedConverter, Servo, ServoPositionConverter, MobileDetector) {

        this.isMobile = function() {
            return MobileDetector.isMobile();
        }

        var setServoPosition = function(data) {
            var position = ServoPositionConverter.convertPosition(data);
            Servo.setServoPosition(position);
        }

        var drive = function(data) {
            var speed = SpeedConverter.convertSpeed(data);
            Engine.setSpeed(speed);
        }

        var stop = function() {
            Engine.sendSpeed(0, 0);
        }

        var joystickL = nipplejs.create({
            zone: document.getElementById('left'),
            mode: 'dynamic',
            color: 'black',
            threshold: 0.9,
            fadeTime: 0,
            size: 120
        });

        var joystickR = nipplejs.create({
            zone: document.getElementById('right'),
            mode: 'dynamic',
            color: 'black',
            threshold: 0.9,
            fadeTime: 0,
            size: 120
        });

        joystickL.on('plain', function (evt, data) {
            setServoPosition(data);
        });

        joystickR.on('removed', function (evt, nipple) {
            stop();
            nipple.off('start move end dir plain');
        }).on('move', function (evt, data) {
            drive(data);
        });
    }]
  });