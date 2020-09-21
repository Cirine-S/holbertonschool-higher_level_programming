#!/usr/bin/node
/*
class Rectangle
*/
'use strict';

let i;
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      return Rectangle === {};
    }
  }

  print () {
    for (i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const rot = this.width;
    this.width = this.height;
    this.height = rot;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
