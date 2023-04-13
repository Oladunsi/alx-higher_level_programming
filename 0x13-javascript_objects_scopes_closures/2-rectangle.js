#!/usr/bin/env node
// creating a rectangle class

module.exports = class Recatangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
  }
};
