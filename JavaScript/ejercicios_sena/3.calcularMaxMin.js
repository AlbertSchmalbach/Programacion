// Función que calcula el máximo y mínimo de un arreglo numérico
function calcularMaxMin(arr) {
    // Spread operator para pasar los elementos a Math.max/Math.min
    const max = Math.max(...arr);
    const min = Math.min(...arr);

    return { max, min };
}

// Ejemplo con arreglo fijo
const arr = [5, 80, 36, 2];
const resultado = calcularMaxMin(arr);
console.log('Mayor array fijo:', resultado.max);
console.log('Menor array fijo:', resultado.min);

// Interacción con el usuario (navegador) - leer números desde prompt
const arrUser = [];
let cantidad = parseInt(prompt('Cuantos numeros vas a ingresar? '));

while (cantidad > 0) {
    const entrada = prompt('Ingrese numero: ');
    const numUser = parseInt(entrada);
    if (numUser) {
        arrUser.push(numUser);
        cantidad--;
    } else {
        alert('Entrada inválida. Inténtalo de nuevo.');
    }
}

console.log('Números ingresados:', arrUser);
const resUser = calcularMaxMin(arrUser);
console.log('Mayor array usuario:', resUser.max);
console.log('Menor array usuario:', resUser.min);



