'use strict';

angular.
  module('raspberryApp').
  config(['$routeProvider',
    function config($routeProvider) {

      $routeProvider.
        when('/', {
            template: '<raspberry></raspberry>'
            }).
        when('/about', {
            templateUrl: 'partials/about.html'
            }).
        when('/404', {
            templateUrl: 'partials/404.html'
            }).
        otherwise({redirectTo: '/404'});
    }
  ]);