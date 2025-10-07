let arr = new Array();
// let arr = [];

let fruits = ["orange", "apple", "lemon",];

console.log(fruits[0]);
console.log(fruits[1]);
console.log(fruits[2]);

fruits[2] = "pears";

console.log(fruits.length);

// ver el ultimo
console.log(fruits[fruits.length-1]);

// otra forma de ver el ultimo
console.log(fruits.at(-1));

// quitar ultimo
console.log(fruits.pop());

// agregar elemento a lo ultimo
fruits.push('pears');

console.log(fruits);

fruits[fruits.length] = "mora";

// extrae el primer elemento
fruits.shift();

console.log(fruits);

fruits.unshift('orange');

arr = fruits;

console.log(arr === fruits);

arr.push('abocado');

console.log(fruits);

for (const fruit of fruits) {
    console.log(fruit);
}

for (const index in fruits) {
    console.log(index); 
}

let num = [1, 2, 3, 4, 5]

num.length = 3;

num.length = 0;

console.log(num);

let nombres = new Array("Luz Saray", "Alberto", "Said");

console.log(nombres);

let matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];

console.log(matrix[1][2]);

let styles = ["Jazz", "Blues"]

styles.push("Rock-n-Roll");

let mitad = Math.floor(styles.length/2);

styles[mitad+1] = "Classics";

console.log(styles.shift());

styles.unshift("Rap", "Reggae");

console.log(styles);

fruits[mitad+1] = "pineaple"
console.log(fruits);



