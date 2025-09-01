// Convertir un objeto a array

const user = {
  name: "Albert",
  life: 99,
  power: 10,
  talk: function() {
    return "Hola!";
  }
};

console.log(Object.keys(user));
console.log(Object.values(user));
console.log(Object.entries(user));

const animals = ["Gato", "Perro", "Burro", "Gallo", "Ratón"];

console.log(Object.keys(animals));
console.log(Object.values(animals));
console.log(Object.entries(animals));

// Convertir un array a objeto

const keys = ["name", "life", "power", "talk"];
const values = ["Albert", 99, 10, function() { return "Hola" }];

const entries = [];

for (const i of Object.keys(keys)) {
    const key = keys[i];
    const value = values[i];
    entries.push([key, value]);
}

console.log(entries);
const users = Object.fromEntries(entries);
const users2 = {...entries};
console.log(typeof users);
console.log(typeof users2);
console.log(users2.constructor.name);