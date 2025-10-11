let numMaquina = Math.floor(Math.random() * (20 - 1)) + 1;

const misNumeros = [5, 7, 12, 18, 20]


for (const miNum of misNumeros) {
    if (numMaquina === miNum) {
    console.log('Haz acertado!!!, el numero es: ', miNum)
} else {
    console.log('Lo siento, no es el numero: ', miNum)
}
}