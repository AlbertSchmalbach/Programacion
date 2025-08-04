// Declaración de un objeto

const objeto = new Object();    // Evitar esta sintaxis en Javascript (no se suele usar)

const myObjeto = {};    // Esto es un objeto vacío

const player = {
  name: "Albert",
  life: 99,
  power: 10,
  getInfo(){
    console.log(`Hola me llamo ${this.name}`);
  },
  toString(){
    console.log(`${this.name} ${this.life} ${this.power}`);
  }
};

// Propiedades de un objeto

console.log(player.name);
console.log(player.life);

console.log(player["name"]);
console.log(player["life"]);


// Añadir propiedades

// FORMA 1: A través de notación con puntos
const avatar = {};

avatar.name = "Albert";
avatar.life = 99;
avatar.power = 10;

// FORMA 2: A través de notación con corchetes
const avatar2 = {};

avatar2["name"] = "Manz";
avatar2["life"] = 99;
avatar2["power"] = 10;

// Métodos de un objeto

player.getInfo()
player.toString()

// Dificultades con notacion de punto

// Notacion punto
const miPropiedad = "City"
player.miPropiedad = "Magangue, Bol."
console.log(player.City);
console.log(player.miPropiedad);

player[miPropiedad] = "Magangue, Bol."
console.log(player.City);

// Constructor de Objetos

function Perfil(nombre, edad, nacionalidad) {
  this.nombre = nombre;
  this.edad = edad;
  this.nacionalidad = nacionalidad;
  this.biografia = function () {
    console.log(
      `Mi nombre es ${this.nombre}. Tengo ${this.edad} años de edad. Soy de ${this.nacionalidad}.`
    );
  };
}

const oladele = new Perfil("Oladele", 50, "Nigeria");
console.log(oladele.biografia()); 

// Crear copias de objetos en JavaScript

// 1. Forma (Utilizar (...)Spreed Operation)

// No es una copia diferente(Hace refencia al mismo espacion memoria)
let objeto4 = {
  nombre: "Alex",
  edad: 40,
};
let objeto5 = objeto4;
console.log(objeto5); // {nombre: 'Alex', edad: 40}
objeto4.nombre = "Jane";
console.log(objeto5); // {nombre: 'Jane', edad: 40}
console.log(objeto4 === objeto5); // true

// Es una copia diferente(no hace refencia al mismo espacion memoria)
let objeto6 = {...objeto5}; 
objeto5.nombre = "Willaims"; 
console.log(objeto5); //{nombre: 'Willaims', edad: 40}
console.log(objeto6); //{nombre: 'Jane', edad: 40}
console.log(objeto5 === objeto6); //false

// 2. Forma (Utilizar el método Object.assign())
let objeto7  = Object.assign({}, objeto6); 
console.log(objeto7); //{nombre: 'Jane', edad: 40}
console.log(objeto7); //{nombre: 'Jane', edad: 40}

console.log(objeto6 === objeto7); //false
objeto6.edad = 60
console.log(objeto6); //{nombre: 'Jane', edad: 60}
console.log(objeto7); //{nombre: 'Jane', edad: 40}

// Iterar Sobre Objetos en JavaScript
for(let llave in objeto) {
    //realizar acción(es) para cada llave
}

let objetoZ = {
  nombre: "Ade",
  Pronombre: "el",
  edad: 60,
};

for (let propiedad in objetoZ) {
  console.log(`${propiedad}: ${objetoZ[propiedad]}`);
}

/* 
nombre: Ade
Pronombre: he
edad: 60
*/