#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
    return list.filter(i => i === searchElement).length;
  };
