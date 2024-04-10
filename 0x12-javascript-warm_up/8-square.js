#!/usr/bin/node

if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const myVar = Number(process.argv[2]);
  let a = 0;
  while (a < myVar) {
      console.log('X'.repeat(myVar));
      a++;
  }
}
