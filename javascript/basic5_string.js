// import the class
const Person = require("./basic7_class");

let day = "tuesday ";
console.log(day.length);
let subDay = day.slice(0, 4);
console.log(subDay);
console.log(day[1]);
// tue day
let splitDay = day.split("s");
console.log(splitDay[1].length);
console.log(splitDay[1].trim().length);

let date = "23";
let nextDate = "27";
let diff = parseInt(nextDate) - parseInt(date);
console.log(diff);
diff.toString();

let newQuote = day + "is Funday day";
console.log(newQuote);
let val = newQuote.indexOf("day", 5); // start from 5th index , meaning skip the day in first word , tuesday
console.log(val);

let count = 0;
let value = newQuote.indexOf("day");
while (value != -1) {
  count++;
  value = newQuote.indexOf("day", value + 1);
}
console.log(count); // shows how may times "day" occurs in the string

let person = new Person("James", "Robbin");
console.log(person.fullName());
