function mediaNumeros(num1, num2) {
    let suma = num1 + num2;

    let media = suma / 2;

    return `La media es:  ${media}`;
}

let num1 = parseInt(prompt('Ingrese un primer numero: '));
let num2 = parseInt(prompt('Ingrese un segundo numero: '));

alert(mediaNumeros(num1, num2))
