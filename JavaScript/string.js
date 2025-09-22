let comillas_simple = 'Soy una comilla simple';
let comilla_doble = "Soy una comilla doble";

let result = `El resultado de 5 x 8 es ${5*8}`;
console.log(result);

console.log("Alberto\nSchmalbach");

console.log(comilla_doble[0]);
console.log(comilla_doble.at(10));
console.log(comilla_doble.slice(0,3));
console.log(comilla_doble.substring(4,15));
console.log(comilla_doble.substr(8,7));

console.log('Albert'.toUpperCase());
console.log('Schmalbach'.toLowerCase());

console.log(comilla_doble.includes('una'));
console.log(comillas_simple.startsWith('S'));
console.log(comilla_doble.endsWith('e'));

