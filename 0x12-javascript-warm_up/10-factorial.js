#!/usr/bin/node

/*
Function to compute the factorial of a number
*/

const argv = process.argv;

// convert the first argument to an integer
const num = Math.floor(Number(argv[2]));

function factorial (n) {
  // Factorial of NaN is 1
  if (isNaN(n)) {
    return 1;
  }

  if (n === 1) {
    return n;
  }

  return n * factorial(n - 1);
}

console.log(factorial(num));
