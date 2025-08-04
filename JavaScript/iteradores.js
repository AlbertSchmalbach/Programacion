const myIterable = [1, 2, 3];
const myIterator = myIterable[Symbol.iterator]();

console.log(myIterator.next());
console.log(myIterator.next());
console.log(myIterator.next());
console.log(myIterator.next());

function* myGeneratorFunction() {
    console.log( "Start of the generator function." );
    yield "First";
    console.log( "Second part of the generator function."  );
    yield "Second";
    console.log( "Third part of the generator function." );
    yield "Third";
};
const myGeneratorObject = myGeneratorFunction();

console.log(myGeneratorObject.next());