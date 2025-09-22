"use strict";

// Objetos literales
const objeto1 = {
  usuario: "Albert",
  nacionalidad: "Colombia",
  profesion: "Programador de Software",
  miBiografia() {
    console.log(
      `Mi nombre es ${this.usuario}. Soy un ${this.profesion} de ${this.nacionalidad}`
    );
  },
};

console.log(objeto1.usuario);
console.log(objeto1.nacionalidad);
console.log(objeto1.profesion);
objeto1.miBiografia();

 const objeto2 = {
  usuario: ["Albert", "James", "Mohammed"],
  profesión: {
    albert: "programador de Software",
    james: "Abogado",
    mohammed: "Escritor técnico",
  },
};

objeto2["resumen"] = `Objeto2 tiene ${objeto2.usuario.length} usuarios`;

console.log(objeto2.usuario);
console.log(objeto2.profesión.albert);
console.log(objeto2["resumen"]);

// Cosntructor de objetos
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

let luzSa = new Perfil('Luz Saray', '23', 'Colombia');
console.log(luzSa.biografia());

// Copiar objetos
const myObjeto = {
    nombre : "Misuris Paola",
    edad : 18,
    aparato: {
    marca: ["apple", "sony"],
    }
}


// const copyObj = myObjeto; // No es copia sino referencia.

// const copyObj = {...myObjeto} // Copia mediante el operador spread - No superficial.

// const copyObj = Object.assign({}, myObjeto); // Copia con Object.assign()- No superficial

const copyObj = structuredClone(myObjeto); // Copia con structuredClone() - Profundo

copyObj.edad = 20;
copyObj.aparato.marca[0] = "Nokia";

console.log(myObjeto);

for (const key in copyObj) {
    if (!Object.hasOwn(copyObj, key)) continue;
    
    console.log(`${key}: ${myObjeto[key]}`);
}
