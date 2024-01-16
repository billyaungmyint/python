console.log("Hello World");
// these are comments

/*
These are also comments
*/

let a = 4;
console.log("a is : " + a);
console.log(typeof a);

let b = 3.14;
console.log(typeof b);

let c = "Billy Aung";
console.log(typeof c);

let required = true;
console.log(typeof required);

c = a + b; // reassigning is allowed with let but not redeclaring - take note of this
console.log(c);
// we cannot redeclare variable let keyword but possible with var
console.log(!required);
