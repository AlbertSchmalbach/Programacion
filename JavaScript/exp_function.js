// const myVariable = function() { };

const myVariable = function myFunction() {
    console.log( "One second elapsed." );
    setTimeout( myFunction, 1000 );
};

// setTimeout( myVariable, 1000 );

// Expresiones de las funciones de flecha

// const myFunction = () => {};

const myFunction = () => 2 + 2

console.log(myFunction());

(function() {
    console.log( "IIFE.")
    }
)();