'use strict';

// Register `settings-controller` component, along with its associated controller and template
angular.
  module('settings').
  component('settings', {
    templateUrl: 'settings-controller/settings-controller.template.html',
    controller: ['$http', 'Path', function SettingsController($http, Path) {

        var self = this;

        this.controllerData = {
            forwardSpeed: 0,
            backSpeed: 0,
            leftOffset: 0,
            rightOffset: 0,
        }
        var ledOn = false;

        this.ledStatus = 'led off';

        this.blinkLed = function() {
            if (!ledOn) {
                ledOn = true;
                $http.get(Path.LED_ON);
                this.ledStatus = 'led on';
            } else {
                ledOn = false;
                $http.get(Path.LED_OFF);
                this.ledStatus = 'led off';
            }
        }

        this.saveInitialData = function() {
            $http.post(Path.INIT_DATA, self.controllerData)
        }

        var getInitialData = function() {
            $http.get(Path.INIT_DATA).then(function(response) {
                self.controllerData = response.data
            });
        }
        getInitialData()
    }]
  });
