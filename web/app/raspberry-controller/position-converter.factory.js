'use strict';

angular.
  module('raspberry').
  factory('PositionConverter', function() {

    var _countPositions = function (minPosition, maxPosition, nrOfSections) {
        var positions = []
        var distance = maxPosition - minPosition;
        var positionLength = distance / (nrOfSections - 1)
        for (var i = 0; i < nrOfSections; i++) {
            positions.push(maxPosition - i * positionLength)
        }
        return positions
    }

    var _countSections = function (nippleRadius, nrOfSections) {
        var sections = []
        for (var i = 0; i < nrOfSections; i++) {
            sections.push(-nippleRadius + i * getSectionLength(nippleRadius, nrOfSections))
        }
        return sections
    }

    var _getPosition = function (positions, sections, nippleRadius, nrOfSections, position) {
        return positions[getSectionNumber(sections, nippleRadius, nrOfSections, position)]
    }

    var getSectionNumber = function (sections, nippleRadius, nrOfSections, position) {
        for (var i = 0; i < nrOfSections; i++) {
            if (sections[i] + getSectionLength(nippleRadius, nrOfSections) >= position) {
                return i;
            }
        }
    }

    var getSectionLength = function (nippleRadius, nrOfSections) {
        var nippleDiameter = nippleRadius * 2
        return Math.floor(nippleDiameter / nrOfSections)
    }

    return {
        countSections: _countSections,
        countPositions: _countPositions,
        getPosition: _getPosition
    }
  });
