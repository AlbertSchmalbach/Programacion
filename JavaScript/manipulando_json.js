// Convertir JSON a objeto

const json = `{
  "name": "Albert",
  "life": 99
}`;

const user = JSON.parse(json);

console.log(user.name);  // "Albert"
console.log(user.life);  // 99

// Convertir objeto a JSON

const player = {
  name: "Albert",
  life: 99,
  talk: function () {
    return "Hola!";
  },
};

const player1 = JSON.stringify(player);       
console.log(player1); // '{"name":"Albert","life":99}'


