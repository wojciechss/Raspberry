'use strict';

angular.
  module('raspberry').
  factory('ServoPositionConverter', ['PositionConverter', function(PositionConverter) {

    var nrOfSections = 5;
    var nippleRadius = 60;
    var sections = []

    var tiltPositions = []
    var minTiltPosition = 55;
    var maxTiltPosition = 115;

    var panPositions = []
    var minPanPosition = 130;
    var maxPanPosition = 180;

    var _convertPanPosition = function (data) {
        var y = Math.sin(data.angle.radian) * data.distance;

        countSections()
        countPanPositions()
        return PositionConverter.getPosition(panPositions, sections, nippleRadius, nrOfSections, y)
    }

    var _convertTiltPosition = function (data) {
        var x = Math.cos(data.angle.radian) * data.distance;

        countSections()
        countTiltPositions()
        return PositionConverter.getPosition(tiltPositions, sections, nippleRadius, nrOfSections, x)
    }

    var countSections = function () {
        if (sections.length !== nrOfSections) {
            sections = PositionConverter.countSections(nippleRadius, nrOfSections)
        }
    }

    var countPanPositions = function () {
        if (panPositions.length !== nrOfSections) {
            panPositions = PositionConverter.countPositions(minPanPosition, maxPanPosition, nrOfSections)
        }
    }

    var countTiltPositions = function () {
        if (tiltPositions.length !== nrOfSections) {
            tiltPositions = PositionConverter.countPositions(minTiltPosition, maxTiltPosition, nrOfSections)
        }
    }

    return {
        convertPanPosition: _convertPanPosition,
        convertTiltPosition: _convertTiltPosition
    }
  }]);
