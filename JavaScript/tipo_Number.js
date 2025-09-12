// formatos cifras
let billion = 1_000_000_000;
let otroBillon = 10e9;
let negativeNum = 25e-2
console.log(otroBillon);
console.log(negativeNum);

// hex (0x...)
console.log(0x92);
// bin (0b...)
console.log(0b1111);
// octal (0o...)
console.log(0o377);

// toString()
let edad = 42;
console.log(edad.toString(2));
console.log(edad.toString(16));

// Math.ceil, Math.floor, Math.round
console.log(Math.ceil(2.54));
console.log(Math.floor(2.54));
console.log(Math.round(2.54));

// toFixed()
pi = 3.1416;
console.log(pi.toFixed(2));

// parseInt() y parseFloat()
console.log(parseInt('100px'));
console.log(parseFloat('12.5em'));

console.log(parseInt('101010', 2));
console.log(parseInt('2a', 16));

// Math.random
console.log(Math.random());
console.log(Math.round(Math.random() * 100));
console.log(Math.min(3, 5, -10, 0, 1));
console.log(Math.max(3, 5, -10, 0, 1));