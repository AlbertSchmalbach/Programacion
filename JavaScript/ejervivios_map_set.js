const a = [4, 5, 8, 9];
const b = [3, 4, 5, 7];
const countries = ["Finland", "Sweden", "Norway", "Spain", "Germany"];

// Ejercicios: Nivel 1

// crear un conjunto vacío
const empty = new Set();

// Crear un conjunto que contenga de 0 a 10 utilizando el bucle
for (let i = 0; i < 11; i++) {
    empty.add(i);   
}

console.log(empty);

// Eliminar un elemento de conjunto
empty.delete(10);
console.log(empty.size);
// Limpia el conjunto
empty.clear();
console.log(empty);
// Crear un conjunto de 5 elementos de cadena a partir de una matriz
const myNumber = new Set(a);
console.log(myNumber);
// Crear un mapa de países y el número de caracteres de un país
const mapCountries = new Map();
mapCountries.set("Argentina", "Buenos aires")
mapCountries.set("Brasil", "Brasilia")
mapCountries.set("Colombia", "Bogota")
console.log(mapCountries);
for(country of mapCountries.keys()){
    console.log(country)
}

// Ejercicios:Nivel 2

// Encontrar una unión b
const c = [...a, ...b]
let C = new Set(c);
console.log(C);
// Encontrar una intersección b
let X = new Set(a);
let Y = new Set(b);

let x = a.filter((num) => Y.has(num));
let z = new Set(x);
console.log(z);

// Encontrar Diferencia a con b
let m = a.filter((num) => !Y.has(num));
let n = new Set(m);
console.log(n);

