const cuadrado = n => n ** 2;

console.log(cuadrado(8));

const user = {
    name: "Said Daniel",
    age: 15,
    info () {
        return `Nombre: ${this.name} - Edad: ${this.age}`
    }
}

console.log(user.info())