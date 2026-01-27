// 🛒 Lista de compras de frutas 🍓🍌🍍
const compras = [];

// 🍏 Pedir la primera fruta
let fruta = prompt('🧺 ¿Qué fruta desea agregar?');
compras.push(fruta);

// ❓ Preguntar si desea agregar más
let consulta = confirm('➕ ¿Desea agregar una fruta más?');

while (consulta) {
    fruta = prompt('🧺 ¿Qué fruta desea agregar?');
    compras.push(fruta);
    consulta = confirm('➕ ¿Desea agregar una fruta más?');
}

// 📋 Mostrar el resultado
console.log('🛒 Usted compró 📄:');

// let numero = 1;
// for (const fruta of compras) {
//     console.log(numero + '. ' + fruta);
//     numero++;
// }

compras.forEach((fruta, index) => console.log(`${index + 1}. ${fruta}`));
