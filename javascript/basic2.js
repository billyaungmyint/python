const flag = true;

// if (!flag) {
//   console.log("condition is satisfied");
// } else {
//   console.log(flag);
//   console.log("condition is not satisfied");
// }

let i = 0;
// while (i < 10) {
//   i++;
//   console.log(i);
// }

// do {
//   i++;
// } while (1 > 10);

// console.log(i);

// 1 to 10 , give me common multiple of 2 and 5
let n = 0;
for (let k = 1; k <= 100; k++) {
  if (k % 2 == 0 && k % 5 == 0) {
    // && = and , || = or
    n++;
    console.log(k);
    if (n == 3) {
      break;
    }
  }
}
