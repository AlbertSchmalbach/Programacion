// Crear un conjunto vacio
const companies = new Set();
console.log(companies);

// Creación de set a partir de array
const languages = [
  "English",
  "Finnish",
  "English",
  "French",
  "Spanish",
  "English",
  "French",
];

const setOfLanguages = new Set(languages);
console.log(setOfLanguages);

for (const lenguages of setOfLanguages) {
    console.log(lenguages);
}

// Añadir un elemento al conjunto
companies.add("Google"); // añadir un elemento a set
companies.add("Facebook");
companies.add("Amazon");
companies.add("Oracle");
companies.add("Microsoft");
console.log(companies.size); // 5 elements in set
console.log(companies);

// mediante un bucle
const arrayCompanies = ["Google", "Facebook", "Amazon", "Oracle", "Microsoft"];
setOfCompanies = new Set();
for (const company of arrayCompanies) {
  setOfCompanies.add(company);
}

console.log(setOfCompanies);

// Borrar un elemento a la vez
console.log(companies.delete("Google"));
console.log(companies.size); // 4 elementos en set

// Comprobación de un elemento en conjunto
console.log(companies.has("Apple")); // false
console.log(companies.has("Facebook")); // true

// Limpiar el conjunto
companies.clear();
console.log(companies);

// Casos practicos
const langSet = new Set(languages);
console.log(langSet); // Set(4) {"English", "Finnish", "French", "Spanish"}
console.log(langSet.size); // 4

const counts = [];
const count = {};

for (const l of langSet) {
  const filteredLang = languages.filter((lng) => lng === l);
  console.log(filteredLang); // ["English", "English", "English"]
  counts.push({ lang: l, count: filteredLang.length });
}
console.log(counts);

const numbers = [5, 3, 2, 5, 5, 9, 4, 5];
const setOfNumbers = new Set(numbers);

console.log(setOfNumbers);

// Unión de conjuntos
let a = [1, 2, 3, 4, 5];
let b = [3, 4, 5, 6];
let c = [...a, ...b];

let A = new Set(a);
let B = new Set(b);
let C = new Set(c);

console.log(C);

// Intersección de conjuntos
let m = [1, 2, 3, 4, 5];
let n = [3, 4, 5, 6];

let M = new Set(m);
let N = new Set(n);

let l = m.filter((num) => N.has(num));
let L = new Set(l);

console.log(L);

// Diferencia de conjuntos
let x = [1, 2, 3, 4, 5];
let y = [3, 4, 5, 6];

let X = new Set(x);
let Y = new Set(y);

let z = x.filter((num) => !Y.has(num));
let Z = new Set(z);

console.log(Z);