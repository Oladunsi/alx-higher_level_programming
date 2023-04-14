#!/usr/bin/node
// creating a rectangle class

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      [this.width, this.height] = [w, h];
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.width = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
