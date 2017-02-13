'use strict';

angular.
  module('raspberryApp').
  config(['$routeProvider',
    function config($routeProvider) {

      $routeProvider.
        when('/', {
            templateUrl: 'partials/home.html'
            }).
        when('/raspberry', {
            template: '<raspberry></raspberry>'
            }).
        when('/led', {
            template: '<led></led>'
            }).
        when('/404', {
            templateUrl: 'partials/404.html'
            }).
        otherwise({redirectTo: '/404'});
    }
  ]);