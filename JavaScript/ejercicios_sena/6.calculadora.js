function imprimirMensaje() { 
    let opcion = prompt(`=== CALCULADORA BASICA ===

        Escoja una operacion:
        1. Sumar.
        2. Restar.
        3. Multiplicar.
        4. Dividir.   
    `);
    return opcion;
}

function sumarNumeros(val1, val2){
    return val1 + val2;
}

function restarNumeros(val1, val2) {
    return val1 - val2;
}

function multiplicarNumeros(val1, val2) {
    return val1 * val2;
}

function dividirNumeros(val1, val2) {
    return val1 / val2;
}

let opcion = imprimirMensaje();
let val1;
let val2;

switch (opcion) {
    case '1':
        val1 = parseInt(prompt(`SUMA
                                Ingrese el primer valor`));
        val2 = parseInt(prompt("Ingrese el segundo valor: "));
        console.log("RESULTADO SUMA: ", sumarNumeros(val1, val2));
        break;
    case '2':
        val1 = parseInt(prompt(`RESTA
                                Ingrese el primer valor`));
        val2 = parseInt(prompt("Ingrese el segundo valor: "));
        console.log("RESULTADO RESTA: ", restarNumeros(val1, val2));
        break;
    case '3':
        
        val1 = parseInt(prompt(`MULTIPLICACION
                                Ingrese el primer valor`));
        val2 = parseInt(prompt("Ingrese el segundo valor: "));
        console.log("RESULTADO MULTIPLICACION: ", multiplicarNumeros(val1, val2));
        break;
    case '4':
        val1 = parseInt(prompt(`DIVISION
                                Ingrese el primer valor`));
        val2 = parseInt(prompt("Ingrese el segundo valor: "));
        console.log("RESULTADO DIVIDIR: ", dividirNumeros(val1, val2));
        break;

    default:
        console.log("Opcion invalida")
        break;
}