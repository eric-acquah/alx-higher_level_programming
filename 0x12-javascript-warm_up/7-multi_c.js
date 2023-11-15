#!/usr/bin/node
/*
Print text a given number times
*/

const argv = process.argv;

const num = Number(argv[2]);

if (!isNaN(num)) {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
