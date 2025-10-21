// Comentarios: este script comprueba si un número es múltiplo de otro.

// Las dos líneas siguientes se usan para probar en el navegador con prompt():
// let num1 = parseInt(prompt("Ingrese un numero entero: "));
// let num2 = parseInt(prompt("Ingrese otro numero entero: "));

// En entornos como Node/VSCode definimos valores de ejemplo directamente.
let num1 = 54;
let num2 = 6;

// Función que determina si num1 es múltiplo de num2
function esMultiplo(num1, num2) {
    // El operador % devuelve el resto de la división entera.
    // Si el resto es 0, entonces num1 es divisible por num2.
    if (num1 % num2 == 0) {
        console.log('Si es multiplo')
    } else {
        console.log('No es multiplo')
    }
}

// Llamada a la función con los valores definidos arriba.
esMultiplo(num1, num2);