const fruits = new Array();
const cities = ['New York', 'Paris', 'Londres', 'Pekin', 'Berlin']

console.log(cities[3]);

// Añadir al array (push y unshift)
fruits.push('Mora');
fruits.push('Sandia');
fruits.unshift('Banana');
console.log(fruits.length);
fruits.concat(['Piña', 'Pera']);
console.log(fruits);

const isArray = Array.isArray(fruits);
console.log(isArray);

const numbers = [12, 10, 5, 80, 25, 3, 15, 18, 20, 47];

let sum = 0;

for (const number of numbers) {
    sum += number
}

console.log(sum);

// Elinimar del array (pop, shift)
console.log(cities.pop());
console.log(cities);

console.log(cities.shift());
console.log(cities);

// map y forEach
const squatersNumber = numbers.map(n => n ** 2);
console.log(squatersNumber);

const lowerCities = cities.map(city => city.toLowerCase());
console.log(lowerCities)

// Ejemplos de uso de forEach con los arrays definidos arriba

// 1) Recorrer fruits mostrando índice y valor
fruits.forEach((fruit, index) => console.log(`Fruta ${index}: ${fruit}`));

// 2) Sumar los valores de numbers usando forEach
let totalWithForEach = 0;
numbers.forEach(n => totalWithForEach += n);
console.log('Total (forEach):', totalWithForEach);



// 4) Reconstruir un array transformado (equivalente a map pero con forEach)
const upperCities = [];
lowerCities.forEach(c => upperCities.push(c.toUpperCase()));
console.log('upperCities:', upperCities);

// 5) Inspeccionar squatersNumber e indicar si cada elemento es par o impar
console.log(numbers.map((n) => n % 2 === 0 ? "par" : "impar"));

// filter y reduce
const numPar = numbers.filter(n => n % 2 === 0);
console.log(numPar)

const suma = numbers.reduce((ac, val)=> ac + val);
console.log(suma);

const nombres = ['Albert', 'Luz Saray', 'Sofia', 'Luz Saray', 'Albert', 'Mario', 'Luz Saray']

const counterNames = nombres.reduce((ac, val) => {
    if (ac[val]) {
        ac[val]++;
    } else {
        ac[val] = 1;
    }
    return ac;
}, {});

console.log(counterNames);

// find() y findIndex()
const firstMayorCinco = numbers.find(n => n > 5);
console.log(firstMayorCinco);

const indexFirstMayorQuince = numbers.findIndex(n => n > 15);
console.log(indexFirstMayorQuince)

const animals = ['conejo', 'lobo', 'camello', 'bufalo', 'tigre']

console.log(animals.slice(2))
console.log(animals.slice(1, 3))
console.log(animals.slice(-2))
console.log(animals.slice(2, -1))