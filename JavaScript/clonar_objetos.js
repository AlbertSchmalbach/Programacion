// copia por valor
let originalValue = 25;
let copyValue = originalValue;

console.log(originalValue);
console.log(copyValue);

copyValue = 40;

console.log(originalValue);
console.log(copyValue);

// copia por referencia
let objectValue = {name: "Alberto", age: 42}

let copyObject = objectValue;

console.log(objectValue);
console.log(copyObject);

copyObject.name = "Luz Saray";

console.log(objectValue);
console.log(copyObject);

// Clonando objetos
const data = {
  name: "Albert",        // Se clona en superficial y en profundidad
  tired: false,           // Se clona en superficial y en profundidad
  likes: ["css", "javascript", "html", "python", "java"], // Sólo en profundidad
  numbers: [4, 8, 15, 16, 23, 42]              // Sólo en profundidad
}

// const copy = data; Esto no realiza una clonación, es una referencia al original

// const copy = {}
// Object.assign(copy, data); Sólo superficial (Hay que crear objeto con el mismo tipo)

// const copy = {...data} Sólo superficial

// ✅ El truco de JSON funciona, ❌ pero estamos limitados a los tipos de JSON
// const str = JSON.stringify(data);
// const copy = JSON.parse(str);

// ✅ Con Lodash, ten en cuenta que necesitaremos descargar/parsear librería externa
// import { cloneDeep } from "lodash-es";
// const copy = cloneDeep(data);

// ✅ Con structuredClone, ciertos tipos (funciones, DOM) devuelven excepción
const copy = structuredClone(data);

console.log(data.name);
console.log(copy.name);

copy.name = "Luz Saray"
copy.likes = ["Gimnasia"]

console.log(data.name);
console.log(copy.name);
console.log(copy.likes);



