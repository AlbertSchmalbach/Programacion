function factorial(n) {
    return n < 2 ? 1: n * factorial(n-1);
}

console.log(factorial(5));
console.log(factorial(7));

const myFactorial = function (n) {
    if (n === 0 || n === 1) return 1;
    else return n * factorial(n-1);
}

console.log(myFactorial(5));
console.log(myFactorial(7));

const otroFactorial = (n) => n < 2 ? 1: n * otroFactorial(n-1);

console.log(otroFactorial(5));
console.log(otroFactorial(7));