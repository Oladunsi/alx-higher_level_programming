#!/usr/bin/node
// creating a square class that inherites from 4-rectanle
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
