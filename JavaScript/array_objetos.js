const equipos = ["Real Madrid", "Barcelona", "Bayer Munich", "Manchester", "Roma"];

function imprimeArray(arr) {
    for (const equipo of arr) {
        console.log(equipo);
    }
}

imprimeArray(equipos);


const objeto1 = {
  usuario: "Alberto",
  nacionalidad: "Colombiano",
  profesion: "Programador de Software",
};

function imprimeObj(obj) {
    const objeto = Object.values(obj);
    const arrayObj = Array(objeto);

    for (const item of arrayObj) {
        console.log(item);
    }
}

imprimeObj(objeto1);