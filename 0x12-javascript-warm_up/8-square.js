#!/usr/bin/node

/*
print a square
*/

const argv = process.argv;

const num = Number(argv[2]);

if (!isNaN(num)) {
  for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
      process.stdout.write('X');
    }
    console.log('');
  }
} else {
  console.log('Missing size');
}
