
let nota = 8.0;

switch (nota) {
    case 10.0:
        console.log("Excelente");
        break;
    case 9.0:
    case 8.0:
    case 7.0:
        console.log("Bueno");
        break;
    case 6.0:
        console.log("Regular");
        break;

    default:
        console.log("Insuficiente");
        break;
}