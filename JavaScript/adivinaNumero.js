let numMaquina = Math.floor(Math.random() * (10 - 1)) + 1;
let vidas = 5;

while (vidas !== 0) {
    let numUsuario = parseInt(prompt("Adivina el numero: "));
    let mensaje =
        numMaquina > numUsuario
            ? "El numero a adivinar es mayor"
            : "El numero a adivinar es menor";
    if (numUsuario === numMaquina) {
        console.log("Ganaste 😎");
        break;
    } else {
        console.log("Perdiste 😫");
        console.log(mensaje);
    }

    vidas--;
}

if (vidas == 0) {
    console.log("Se te agotaron las vidas");
}
