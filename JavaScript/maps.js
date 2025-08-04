// const map = new Map();
// console.log(map);

// Creación de un mapa a partir de una matriz
countries = [
  ["Finland", "Helsinki"],
  ["Sweden", "Stockholm"],
  ["Norway", "Oslo"],
];

const map = new Map(countries);
console.log(map);
console.log(map.size);

// Añadir valores al mapa
const countriesMap = new Map();
console.log(countriesMap.size); // 0
countriesMap.set("Finland", "Helsinki");
countriesMap.set("Sweden", "Stockholm");
countriesMap.set("Norway", "Oslo");
console.log(countriesMap);
console.log(countriesMap.size);

// Obtención de un valor de Mapa
console.log(countriesMap.get("Finland"));

// Comprobar clave en el mapa
console.log(countriesMap.has("Finland"));

for (const country of countriesMap) {
  console.log(country);
}

for (const [country, city] of countriesMap) {
  console.log(country, city);
}