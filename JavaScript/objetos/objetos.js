const programmer = {
    name: "Albert Schmalbach",
    age: 42,
    stack: {
        lenguages: ['python', 'java', 'javascript', 'c++', 'php'],
        experience: 2
    },

    info() {
        return `
        Nombre: ${this.name}
        Lenguajes: ${this.stack.lenguages.join(', ')}
        Experiencia: ${this.stack.experience} años`
    }

}

// console.log(programmer.stack.lenguages);
console.log(programmer.info());