#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
// let's sort the array and take the second element :
  const second = process.argv.sort(function (a, b) { return b - a; })[3];
  console.log(second);
}
