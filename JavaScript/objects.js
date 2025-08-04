const user = {
    name: "Albert",
    lenguages: {
        frontend:["HTML", "CSS", "JS"], 
        backend: ["PYTHON", "PHP", "JAVA"]
    },
    city: "Magangue, Bol.",
    getInfo() {
        console.log(`${this.name} es programador(a) de ${this.lenguages}. El(Ella) es de ${this.city}`);
    },
    otro: null
}


console.log(user.name);
console.log(user["lenguages"]);

const copyUser1 = user; // Modifica el el original
const copyUser2 = Object.assign({}, user); // Copia aparte. No modifica el original

// copyUser1.name = "Luz Saray";
copyUser2.name = "Luz Saray";

console.log(user);

user.getInfo();
copyUser2.getInfo();


// Con ternario
console.log(user.lenguages?user.lenguages.frontend:undefined);

// Con ecadenamiento opcional
console.log(user?.lenguages?.backend);

// Con and(&&)
console.log(user.lenguages && user.lenguages.frontend);

// Con metodos
user.getInfo?.();

console.log(user?.["otro"]);

delete user?.otro;

console.log(user);