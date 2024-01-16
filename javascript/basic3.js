// this is 1 way
// let marks = Array(6);
// marks = new Array(20, 40, 35, 12, 37,100);

let marks = [20, 40, 35, 12, 37, 100];
// console.log(marks[2]);
// marks[3] = 14;
// console.log(marks);
// console.log(marks.length); // length of the array
// marks.push(65); // add at the end
// console.log(marks);
// marks.pop(); // remove the last element
// console.log(marks);
// marks.unshift(12); // add at the beginning
// console.log(marks);
// console.log(marks.indexOf(100)); // find the location of the value index + 1
// console.log(marks.includes(40)); // check if the value is part of the array
// console.log(marks.slice(2, 5)); // last index is not included - so it is from 2nd to 4th

let sum = 0;
for (let i = 0; i < marks.length; i++) {
  //   console.log(marks[i]);
  sum += marks[i];
}
console.log("sum is : " + sum);

// reduce filter map

let total = marks.reduce((sum, mark) => sum + mark, 0); // same logic as for loop ... mark is each value from marks array and add to sum
console.log("total is : " + total);

let scores = [12, 13, 14, 16];
// print element of array which are even numbers
let newFilteredScore = scores.filter((score) => score % 2 == 0);
console.log(newFilteredScore);

let mappedArray = newFilteredScore.map((score) => score * 3);
console.log(mappedArray);

let totalVal = mappedArray.reduce((sum, val) => sum + val, 0);
console.log(totalVal);

let scores1 = [12, 003, 13, 14, 16];
let sumValue = scores1
  .filter((score) => score % 2 == 0)
  .map((score) => score * 3)
  .reduce((sum, val) => sum + val, 0); // 0 is the initial value and its optional .. try removing it or change it to 1 , total wwill increase by 1
console.log(sumValue);

let fruits = ["banana", "mango", "pomrgrante", "apple"];
fruits.sort(); // can only sort the strings
console.log(fruits);

console.log(scores1.sort((a, b) => a - b));

fruits.reverse();
console.log(fruits);
