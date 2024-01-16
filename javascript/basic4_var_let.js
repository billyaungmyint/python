// block of code
// var - global/functional scope
// let - global/block level {}

function add(num1, num2) {
  return num1 + num2;
}
let sum = add(2, 3);
console.log(sum);

// annoymous functions , do not have names -- function expressions

let sumOfIntergers = function (c, d) {
  return c + d;
};

let sumOfNumbers = (c, d) => c + d;
console.log(sumOfNumbers(3, 4));
