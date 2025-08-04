// if... else
// if ( true ) console.log( "True." );

// if ( true ) {
//     const myString = "True.";
//     console.log( myString );
// }

// if ( false ) console.log( "True." );

// if ( false ) console.log( "True." );
// else console.log( "False" );

// const myCondition = 2;
// if ( myCondition === 5 ) console.log( "Five." );
// else if ( myCondition === 2 ) console.log( "Two." );

// if ( myCondition === 5 ) {
//     console.log( "Five." );
// } else if ( myCondition === 3 ) {
//     console.log( "Three" );
// } else {
//     console.log( "Neither five nor three." );
// }

// Ternario
// const myFirstResult  = true  ? "First value." : "Second value.";
// const mySecondResult = false ? "First value." : "Second value.";

// console.log(myFirstResult);
// console.log(mySecondResult);

// switch... case
// switch ( 20 ) {
//     case 5:
//         console.log( "The value was five." );
//         break;
//     case 10:
//         console.log( "The value was ten." );
//         break;
//     default:
//         console.log( "The value was something unexpected." );
// }

// Iteraciones y bucles

// while
let iterationCount = 0;
while( iterationCount < 3 ) {
  iterationCount++;
  console.log( `Loop ${ iterationCount }.` );
}

let randomize = () => Math.floor( Math.random() * 10 );
let randomNum = randomize();
while( randomNum !== 7 ){
  console.log( `The number is not ${ randomNum }.` );
  randomNum = randomize();
}

console.log( `The correct number, ${ randomNum }, was found.` );

// do...while
let randoNum;
do {
  randoNum = ( () => Math.floor( Math.random() * 10 ) )();
  console.log( `Is the number ${ randoNum }?` );
} while ( randoNum !== 7 );

console.log( `Yes, ${ randoNum } was the correct number.` );

// for
for( let i = 0; i < 3; i++ ) {
  console.log( "This loop will run three times.")
}

// for...of
const myIterable = [ "Luz Saray", "Misuris", "Daniela" ];
for( const myElement of myIterable ) {
  console.log( myElement );
}

// for... in...
const myObject = { "profetion" : "Programer", "Status" : "Single" };
for( const myKey in myObject ) {
  console.log( myKey );
}

// forEach()
const lenguages = ['Python', 'JavaScript', 'Java', 'Ruby', 'PHP']
console.log('Lenguajes mas demandados:');
lenguages.forEach((element, i, array)=>{
  console.log(i+1, element);
});

