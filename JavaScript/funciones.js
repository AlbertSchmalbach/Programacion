// funciones declarativa

function numeroAleatorio(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}

// funciones expresada
const numAzar = function(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}

let numeroAzar = numeroAleatorio(1,20);

console.log(numeroAzar);
console.log(numAzar(100,200));

// funciones flecha
const numAzarFlecha = (min, max) => Math.floor(Math.random() * (max - min)) + min;

console.log(numAzarFlecha(1000, 2000));