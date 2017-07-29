'use strict';

// Register `raspberry-controller` component, along with its associated controller and template
angular.
  module('raspberry').
  component('raspberry', {
    templateUrl: 'raspberry-controller/raspberry-controller.template.html',
    controller: ['Engine', 'Servo', 'ServoPositionConverter', 'MobileDetector',
        function RaspberryController(Engine, Servo, ServoPositionConverter, MobileDetector) {

        this.isMobile = function() {
            return MobileDetector.isMobile();
        }

        this.getCameraHostname = function() {
            return 'http://' + window.location.hostname + ':8081';
        }

        var setPanPosition = function(data) {
            var panPosition = ServoPositionConverter.convertPanPosition(data);
            Servo.setPanPosition(panPosition);
        }

        var setTiltPosition = function(data) {
            var tiltPosition = ServoPositionConverter.convertTiltPosition(data);
            Servo.setTiltPosition(tiltPosition);
        }

        var drive = function(data) {
            Engine.setSpeed(data);
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

        joystickL.on('move', function (evt, data) {
            setPanPosition(data);
            setTiltPosition(data);
        });

        joystickR.on('removed', function (evt, nipple) {
            stop();
            nipple.off('start move end dir plain');
        }).on('move', function (evt, data) {
            drive(data);
        });
    }]
  });
