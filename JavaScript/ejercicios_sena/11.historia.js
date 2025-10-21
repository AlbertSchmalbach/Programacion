// Definimos el procedimiento
function contarHistoria(nombre, apellido, lugar) {
  console.log("\n--- Pequeña Historia ---");
  console.log(`Había una vez una persona llamada ${nombre} ${apellido},`);
  console.log(`que vivía en un hermoso lugar llamado ${lugar}.`);
  console.log(`Un día, ${nombre} decidió hacer algo que cambiaría su vida para siempre... estudiar programacion en el Sena`);
  console.log(`Desde ese día, los habitantes de ${lugar} siempre recordaron a ${nombre} ${apellido}.`);
  console.log("--------------------------");
}

// Pedimos los datos al usuario
let nombre = prompt("Ingrese su nombre:");
let apellido = prompt("Ingrese su apellido:");
let lugar = prompt("Ingrese un lugar:");

// Llamamos al procedimiento
contarHistoria(nombre, apellido, lugar);
