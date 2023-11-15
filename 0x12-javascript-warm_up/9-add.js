#!/usr/bin/node

/*
print the sum of two numbers
*/

const argv = process.argv;

function add (a, b) {
  a = Number(a);
  b = Number(b);

  return Math.floor(a + b);
}

console.log(add(argv[2], argv[3]));
