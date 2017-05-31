'use strict';

// Register `raspberry-controller` component, along with its associated controller and template
angular.
  module('raspberry').
  component('raspberry', {
    templateUrl: 'raspberry-controller/raspberry-controller.template.html',
    controller: ['SpeedConverter', 'Engine', function RaspberryController(SpeedConverter, Engine) {

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
            size: 100
        });

        var joystickR = nipplejs.create({
            zone: document.getElementById('right'),
            mode: 'dynamic',
            color: 'black',
            size: 100
        });

        joystickR.on('removed', function (evt, nipple) {
            stop();
            nipple.off('start move end dir plain');
        }).on('move', function (evt, data) {
            drive(data);
        });
    }]
  });
