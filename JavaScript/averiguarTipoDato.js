// Primitive
const text = "Hola ManzDev!";
console.log(typeof text);
console.log(text.constructor.name);

    
const number = 42;
console.log(typeof number);
console.log(number.constructor.name);


const boolean = true;
console.log(typeof boolean);
console.log(boolean.constructor.name);


let notDefined;
console.log(typeof notDefined);
// console.log(notDefined.constructor.name); // No define este tipo


let tipoNull = null;
console.log(tipoNull);
// console.log(tipoNull.constructor.name); // No define este tipo


// Not primitive
const numbers = [1, 2, 3, 4];
console.log(typeof numbers);
console.log(numbers.constructor.name)

const user = { name: "ManzDev" };
console.log(typeof user);
console.log(user.constructor.name);




