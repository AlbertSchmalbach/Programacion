function hacerLogin(nameUser, pass) {
    let sesion = false;
    let mensaje ="";
    // Usar igualdad estricta 
    if (nameUser === "usuario1" && pass === "asdasd") {
        sesion = true;
    } else {
        mensaje = "Credenciales incorrectas";
    }
    return {mensaje, sesion};
}

let intentos = 3;
let sesion = false;
// Continuar mientras haya intentos y NO se haya hecho sesion
while (intentos > 0 && !sesion) {
    let user = prompt("Ingrese su nombre usuario: ");
    // // let user = "usuario1";
    let pass = prompt("Ingrese su contraseña: ");
    // let pass = "asdasd";

    const login = hacerLogin(user, pass);
    sesion = login.sesion;
    console.log(login.mensaje);

    // Si no se autenticó, reducir intentos y mostrar restante
    if (!sesion) {
        intentos--;
        console.log(`Intentos restantes: ${intentos}`);
        if (intentos === 0) {
            intentos = parseInt(prompt("Dame otro numero de intentos: "))
        }
    }
}

if (sesion) {
    console.log('Login correcto!!!😎...Acceso concedido.');
} else {
    console.log('Se han agotado los intentos. Acceso denegado.');
}


