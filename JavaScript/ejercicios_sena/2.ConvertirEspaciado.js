// Función que toma una cadena y la imprime con un espacio extra entre cada carácter.

function ConvertirEspaciado(texto) {
    // Empezamos con un espacio inicial para que la salida quede centrada como en el ejemplo
    let textoEspaciado = " ";

    // Recorremos cada carácter de la cadena de entrada usando for..of
    for (const letter of texto) {
        // Añadimos el carácter y un espacio a la cadena de salida
        textoEspaciado += letter + " ";
    }
    // Imprimimos el resultado en consola
    console.log(textoEspaciado);
}

// Llamada de ejemplo: cambia el argumento por cualquier otra cadena para probar
ConvertirEspaciado('Hola, tu.');