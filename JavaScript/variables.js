let myVariable = 5;

myVariable + myVariable

let firstVariable,
     secondVariable,
     thirdVariable;

// const myConstant = true;

const constantObject = { "firstvalue" : true };

console.log(constantObject);

constantObject.secondvalue = false;

console.log(constantObject);

// Alcance del bloque

{
    let scopedVariable = true;
    console.log( scopedVariable );
}

// console.log( scopedVariable ); // Error de scope

{
  const myConstant = false;
  console.log(myConstant); 
}
const myConstant = true;
console.log(myConstant);

// Alcance de la función
function myFunction() {
    var scopedVariable = true;

    return scopedVariable;
}

// Alcance global

var functionGlobal = true; // Global
let blockGlobal = true; // Global

{
    console.log( blockGlobal );
    console.log( functionGlobal );
}


(function() {
    console.log( blockGlobal );
    console.log( functionGlobal );
}());

function myFunction() {
    globalVariable = "global";

    return globalVariable
}

console.log(myFunction())
console.log(globalVariable)

pointNumber = 5;

var pointNumber;

console.log(pointNumber);



