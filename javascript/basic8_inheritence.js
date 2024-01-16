const Person = require("./basic7_class");

class Pet extends Person {
  //   get location() {
  //     return "BlueCross";
  //   }
  constructor(firstName, lastName) {
    // call parent class constructor
    super(firstName, lastName);
  }
}

let pet = new Pet("Sam", "Potter");
console.log(pet.fullName());
console.log(pet.location);
