console.log("El clasico console.lg()");

console.warn("Advertencia");
console.error("Error");

console.group("Chicas: ")
console.log("Luz Saray");
console.log("Misury Paola");
console.groupEnd();

const users = [
  { name: "Manz", role: "streamer", status: "happy" },
  { name: "BlurSoul_", role: "mod", status: "happy" },
  { name: "felixicaza", role: "mod", status: "happy" },
  { name: "pheralb", role: "mod", status: "porosad" }
];

console.table(users);

// console.log({ name, role, status });

console.assert(5 < 10, "5 es menor que 10");
// No ocurre nada

console.assert(5 < 0, "5 es menor que 0");
// Muestra el mensaje indicado con un aviso de error


// console.dir(document.body);

for (let i = 0; i < 5; i++) {
  console.count("test-loop");
}
// console.countEnd("test-loop");

console.time("test1");
for (let i = 0; i < 10; i++) {
  /* Operación costosa */
  console.timeLog("test1", i);
}
console.timeEnd("test1");

const numero = +"42"

console.log(typeof numero)
