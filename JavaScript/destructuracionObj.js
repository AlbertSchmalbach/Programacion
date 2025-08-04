const user = {
    name: "Albert",
    rol: "Programmer",
    lenguage: ["Python", "Java", "JavaScript"],
    points: 80
}

// const {name, rol, lenguage} = user;
// const {name, rol: profetion, lenguage} = user;

// console.log(name);
// console.log(lenguage);
// console.log(profetion);

const fullUser = {
    ...structuredClone(user),
    city: "Magangue"
}
fullUser.lenguage[1] = "PHP";
console.log(user.lenguage);
console.log(fullUser.lenguage);

const {name, ...rest} = user;
console.log(name);
console.log(rest);

function show({name, rol, points}) {
    const start = "⭐".repeat(points/20);
    return `Name: ${name} (${rol}) ${start}`
}

console.log(show(user));