function numeroletras(n) {
    const wordNums = {
        1:'uno', 
        2:'dos', 
        3:'tres', 
        4:'cuatro', 
        5:'cinco', 
        6:'seis', 
        7: 'siete', 
        8:'ocho', 
        9: 'nueve', 
        10: 'diez'
    };
    if (n > 0 && n <= 10) {
        // n-=1;
       return wordNums[n];
    } else {
        return 'Numero no valido';
    }
}

// let numero = parseInt(prompt("Ingresa un numero"))
let numero = 7;
console.log(numeroletras(numero));
// alert(numeroletras(numero));