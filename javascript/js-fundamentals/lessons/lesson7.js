let cars = ["Volvo", "Toyota", "Tesla"];

for (let car of cars) {
  console.log(car);
  if (car == "Toyota") {
    break;
  }
}

cars.forEach((car) => {
  console.log(car);
});
