const numeros = [12, 5, 80, 30, 2, 24, 7]

numeros.join(',');

console.log(numeros.sort());

// let ordenaMenorMayor = (a, b) => a - b;
// let ordenaMayorMenor = (a, b) => b - a;

// Ordenar array menor a mayor
console.log(numeros.sort((a, b) => a - b));
// Ordenar array mayor a menor
console.log(numeros.sort((a, b) => b - a));

const data = [
    {user: 'Mariela', age: 31, rol: 'SAC'},
    {user: 'Eduardo', age: 30, rol: 'CEO'},
    {user: 'Diana', age: 28, rol: 'Designer'},
    {user: 'Andres', age: 34, rol: 'Project Manager'},
    {user: 'Sofia', age: 24, rol: 'Programmer'},
]

data.sort((a, b) => {
    return a.age - b.age;
})

for (const users of data) {
    console.log(users.user, users.age);
}

console.log(data.filter(element => element.age > 30));