"use strict";

angular.
  module("ngTouch", []).
  directive("ngTouchstart", function () {
    return {
      controller: function ($scope, $element, $attrs) {
        $element.bind('touchstart', onTouchStart);
        $element.bind('mousedown', onTouchStart);

        function onTouchStart(event) {
          var method = $element.attr('ng-touchstart');
          $scope.$event = event;
          $scope.$apply(method);
        };
      }
    };
  }).
  directive("ngTouchend", function () {
    return {
      controller: function ($scope, $element, $attrs) {
        $element.bind('touchend', onTouchEnd);
        //$element.bind('mouseup', onTouchEnd);

        function onTouchEnd(event) {
          var method = $element.attr('ng-touchend');
          $scope.$event = event;
          $scope.$apply(method);
        };
      }
    };
  }
 );