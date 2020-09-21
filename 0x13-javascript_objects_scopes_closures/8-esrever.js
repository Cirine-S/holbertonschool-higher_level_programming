#!/usr/bin/node
exports.esrever = function (list) {
    const arr = [];
    let i;
    for (i = list.length - 1; i >= 0; i--) {
      arr.push(list[i]);
    }
    return arr;
  };
