const enemies = [
  { id: "SKELETON", name: "Esqueleto" },
  { id: "SPECTRE", name: "Espectro" },
  { id: "GHOST", name: "Fantasma" }
];

const SKELETON = Symbol("SKELETON");
const SPECTRE = Symbol("SPECTRE");
const GHOST = Symbol("GHOST");


const enemies2 = [
  { id: SKELETON, name: "Esqueleto" },
  { id: SPECTRE, name: "Espectro" },
  { id: GHOST, name: "Fantasma" }
];


const addEnemy = (id, name) => enemies2.push({ id, name });
const findEnemyById = (id) => enemies2.find(enemy => enemy.id === id);

// Añadimos nuevo esqueleto a la lista de enemigos
addEnemy("SKELETON", "Esqueleto resplandeciente");

console.log(findEnemyById("SKELETON"));
// Devuelve { id: "SKELETON", name: "Esqueleto" }



// Añadimos nuevo esqueleto a la lista de enemigos
const GLEAMING_SKELETON = Symbol("SKELETON");
addEnemy(GLEAMING_SKELETON, "Esqueleto resplandeciente");

console.log(findEnemyById(GLEAMING_SKELETON))
console.log(findEnemyById(SKELETON))

