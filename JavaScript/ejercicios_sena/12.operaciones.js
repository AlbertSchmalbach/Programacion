function imprimirMensaje() {
    let opcion = prompt(`=== OPERACIONES BASICAS ===

        Escoja una operacion:
        1. Sumar.
        2. Restar.
        3. Multiplicar.
        4. Dividir.   
    `);
    return opcion;
}

function sumarNumeros(val1, val2) {
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

function main() {
    let opcion = imprimirMensaje();
    let val1;
    let val2;

    switch (opcion) {
        case '1':
            alert("SUMA");
            val1 = parseInt(prompt("Ingrese el primer valor"));
            val2 = parseInt(prompt("Ingrese el segundo valor: "));
            console.log("RESULTADO SUMA: ", sumarNumeros(val1, val2));
            break;
        case '2':
            alert("RESTA")
            val1 = parseInt(prompt("Ingrese el primer valor"));
            val2 = parseInt(prompt("Ingrese el segundo valor: "));
            console.log("RESULTADO RESTA: ", restarNumeros(val1, val2));
            break;
        case '3':
            alert("MULTIPLICACION")
            val1 = parseInt(prompt("Ingrese el primer valor"));
            val2 = parseInt(prompt("Ingrese el segundo valor: "));
            console.log("RESULTADO MULTIPLICACION: ", multiplicarNumeros(val1, val2));
            break;
        case '4':
            alert("DIVISION")
            val1 = parseInt(prompt("Ingrese el primer valor"));
            val2 = parseInt(prompt("Ingrese el segundo valor: "));
            console.log("RESULTADO DIVIDIR: ", dividirNumeros(val1, val2));
            break;

        default:
            console.log("No existe operacion con ese numero.")
            break;
    }
}

main();