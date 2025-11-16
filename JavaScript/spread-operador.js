// copy

const originalArray = ['python', 'java', 'c++', 'javascript', 'php']

const copyArray = [...originalArray]

console.log(originalArray)
console.log(copyArray)

// combinar
const array1 = [1, 2, 3]
const array2 = [4, 5, 6]
const combineArray = [...array1, ...array2]

console.log(combineArray)

// adicionar elemento
const baseArray = [1, 2, 3]
const arrayAdicionalElement = [...baseArray, 4, 5, 6, 7]

console.log(arrayAdicionalElement)

// con funciones

function sum(...nums) {
    let suma = 0;
    for (const num of nums) {
        suma+= num;
    }

    return suma
}

let resultado = sum(10, 40, 80, 15) 

console.log(resultado)