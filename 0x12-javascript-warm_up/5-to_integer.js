#!/usr/bin/node
/*
Convert arguments to integers if possible
*/

const argv = process.argv;

const num = Number(argv[2]);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Math.floor(num));
}
