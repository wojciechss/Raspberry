'use strict';

angular.
  module('raspberry').
  factory('ServoPositionConverter', function() {

    const nrOfSections = 3;

    const nippleRadius = 60;
    const nippleDiameter = nippleRadius * 2
    const sectionLength = Math.floor(nippleDiameter / nrOfSections)
    var sections = []

    const minPosition = 60;
    const maxPosition = 120;
    const distance = maxPosition - minPosition;
    const positionLength = distance / (nrOfSections - 1)
    var positions = []

    var countPositions = function () {
        if (positions.length == nrOfSections) {
            return;
        }
        for (var i = 0; i < nrOfSections; i++) {
            positions.push(maxPosition - i * positionLength )
        }
    }

    var countSections = function () {
        if (sections.length == nrOfSections) {
            return;
        }
        for (var i = 0; i < nrOfSections; i++) {
            sections.push(-nippleRadius + i * sectionLength)
        }
    }

    var getSectionNumber = function (x) {
        for (var i = 0; i < nrOfSections; i++) {
            if (sections[i] + sectionLength >= x) {
                return i;
            }
        }
    }

    var _convertPanPosition = function (data) {
        if (data.direction.y === 'up') {
            return 130;
        } else if (data.direction.y === 'down') {
            return 180;
        }
    }

    var _convertTiltPosition = function (data) {
        var acceleration = data.distance;
        var x = Math.cos(data.angle.radian) * acceleration;
        countSections()
        countPositions()
        return positions[getSectionNumber(x)]
    }

    return {
        convertPanPosition: _convertPanPosition,
        convertTiltPosition: _convertTiltPosition
    }
  });