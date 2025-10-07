// splice
const arr = ['Casa', 12, true, 'Ave', 'Cartagena']
delete arr[arr.length-1]
console.log(arr.length);
arr.splice(0,3);
console.log(arr.length);
arr.splice(0, 2, 'Gato', 1500);
console.log(arr);
arr.splice(2, 0, true, 'Avion');
console.log(arr);

// slice
const vocales = ['a', 'e', 'i', 'o', 'u']
console.log(vocales.slice(0, 3));
copyArr = vocales.slice()
console.log(copyArr);

// concat
const arrTotal = arr.concat(vocales);
console.log(arrTotal);



