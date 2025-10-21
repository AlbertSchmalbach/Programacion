const text = "Lenguaje de programacion";

console.log(text.constructor.name);

const proto1 = Object.getPrototypeOf(text);
console.log(proto1);

const proto2 = Object.getPrototypeOf(proto1);
console.log(proto2.constructor.name);

const proto3 = Object.getPrototypeOf(proto2);
console.log(proto3);

// Por lo tanto, la cadena de prototipos de este objeto es:
// 'String' > 'Object' > null