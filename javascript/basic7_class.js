//export the class
module.exports = class Person {
  age = 25; // class variable
  // this is a property
  get location() {
    return "canada";
  }

  //constructor is a method which executes by default when you create object of the class
  constructor(firstName, lastName) {
    this.firstName = firstName;
    this.lastName = lastName;
  }
  // this is a method
  fullName() {
    console.log(this.firstName + " " + this.lastName);
  }
};

// let person = new Person("Tom", "Jones");
// let person1 = new Person("Jim", "Carrey");
// console.log(person.age);
// console.log(person.location);
// console.log(person.fullName());
// console.log(person1.fullName());
