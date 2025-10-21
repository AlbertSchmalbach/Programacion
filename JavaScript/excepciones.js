let numerador = 12;
let denominador = 3;
var resultado = null;

try {
    if (denominador == 0) {
        throw new Error("No se puede dividir por cero");
    } else {
        resultado = numerador/denominador;
        console.log(resultado);
    }
} catch (error) {
    console.error(error);
    resultado = null;
}