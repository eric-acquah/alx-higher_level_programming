#!/usr/bin/node

/*
Search for the second biggest number
*/

const argv = process.argv;

function secondBiggest (list) {
  let prevMax = Math.floor(Number(list[3]));
  let currentMax = Math.floor(Number(list[2]));

  for (let i = 2; i < list.length; i++) {
    // convert current value to integer
    const val = Math.floor(Number(list[i]));

    if (currentMax < val) {
      // Give the previous largest value to prev_max
      prevMax = currentMax;
      // store the currently largest
      currentMax = val;
    } else if ((prevMax < val) && (val !== currentMax)) {
      // (prevMax !== undefined) && (prevMax < val)
      // if the stored largest value is still larger yet currently read value is
      // larger than the second largest, then store the given value
      // as the second largest
      prevMax = val;
    }
  }

  return prevMax;
}

if (argv.length <= 3) {
  console.log('0');
} else {
  console.log(secondBiggest(argv));
}
