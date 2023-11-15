#!/usr/bin/node
/*
Print the first argument passed to the program
*/

const argv = process.argv;

if (argv[2]) {
  console.log(argv[2]);
} else {
  console.log('No argument');
}
