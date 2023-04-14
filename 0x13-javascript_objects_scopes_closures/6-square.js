#!/usr/bin/node
// creating a square class that inherites from 4-rectanle
const square = require('./5-square');
class Square extends square {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    this.print(c);
  }
}
module.exports = Square;
