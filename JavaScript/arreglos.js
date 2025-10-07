const chicas = ['Luz Saray', 'Misuris Paola', 'Yulianis Marcela']

console.log(chicas);
console.log(chicas.length);
console.log(chicas[0]);

for (let i = 0; i < chicas.length; i++) {
    const element = chicas[i];
    console.log(element);
}

for (const chica of chicas) {
    console.log(chica)
}