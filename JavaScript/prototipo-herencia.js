class Animal {
    constructor(nombre, tipo) {
        this.nombre = nombre;
        this.tipo = tipo;
    }

    emitirSonido (){
        return 'El animal tiene un sonido';
    }
}

class Perro extends Animal {
    constructor(nombre, tipo, raza) {
        super(nombre, tipo);
        this.raza = raza;
    }

    emitirSonido(){
        return 'El perro ladra';
    }

    correr(){
        return `${this.nombre} corre alegremente`;
    }
}

const perro1 = new Perro('Firulays', 'Perro', 'Labrador');

console.log(perro1.emitirSonido());
console.log(perro1.correr());

Perro.prototype.Nuevometodo = function () {
    console.log('Nuevo metodo de la clase');
}

perro1.Nuevometodo();
console.log(Perro)