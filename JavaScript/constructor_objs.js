function Persona(nombre, apellido, edad) {
    this.nombre = nombre;
    this.apellido = apellido;
    this.edad = edad;
}


const persona1 = new Persona('Alberto', 'Schmalbach', 42);
const persona2 = new Persona('Luz Saray', 'Atencia', 23);

console.log(persona1);
console.log(persona2);

Persona.prototype.ciudad = "Magangue";

persona1.telefono = "3043830143";
persona2.telefono = "3234719486";

console.log(persona1);
console.log(persona2);

Persona.prototype.info = function () {
    return `
        Nombre : ${this.nombre}
        Edad: ${this.edad}
        Telefono: ${this.telefono}
        ciudad: ${this.ciudad}    
        `
}

console.log(persona1.info());