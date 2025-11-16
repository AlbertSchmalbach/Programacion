class Libro {
    constructor(titulo, genero, autor, precio) {
        this.titulo = titulo
        this.genero = genero
        this.autor = autor
        this.precio = precio
    }

    info(){
        return `El libro ${this.titulo} tiene un costo de ${this.precio}.`
    }
}

const libro1 = new Libro('Cien años de soledad', 'Novela', 'Gabriel Garcia Marquez', '10 USD');
const libro2 = new Libro('Frankenstein', 'Terror', 'Mary Shelley', '5 USD');
const libro3 = new Libro('Don Quijote de la Mancha', 'Novela', 'Miguel de Cervantes', '7.5 USD');

console.log(libro1.info());