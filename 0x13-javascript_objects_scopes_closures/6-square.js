#!/usr/bin/node
const SquareParent = require('./5-square');

class Square extends SquareParent {
  charPrint (c) {
    let i;
    if (c === undefined) {
      c = 'X';
    }
    for (i = 0; i < this.height; i++) {
      console.log((c).repeat(this.height));
    }
  }
}

module.exports = Square;
