// funcion simple
function saludar() {
    console.log("Saludar des Javascript");
    
}

saludar();

// Declaración de la función con parametro
function tablaMultiplicar(n=1) {
  for (let i = 0; i <= 10; i++) console.log(n + " * "+ i, "="+ n * i );
}

// ejecutar funcion tablaMultiplicar
tablaMultiplicar(7);

// Con 2 parametros
function suma(a,b) {
    return a + b;
}

console.log(suma(40, 23));

