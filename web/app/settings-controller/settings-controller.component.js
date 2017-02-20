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
            rightOffset: 0
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
