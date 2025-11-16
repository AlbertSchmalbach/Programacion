const userDataBase = [
    {
        username: 'Paula',
        password: '123'
    },

    {
        username: 'Juan',
        password: '456'
    },

    {
        username: 'Karo',
        password: '789'
    }
]

const usersTimeline = [
    {
        username: 'Estefany',
        timeline: 'Me encanta Javascript!'
    },

    {
        username: 'Oscar',
        timeline: 'Developer es lo mejor'
    },

    {
        username: 'Dayan',
        timeline: 'A mi me encanta el cafe'
    },

    {
        username: 'Albert',
        timeline: 'Quiero trabajar'
    }
]

function usuarioExistente(username, passwd) {
    for (let i = 0; i < userDataBase.length; i++) {
        if (userDataBase[i].username === username && userDataBase[i].password === passwd) {
            return true;
        }
    }
    return false;
}

function signIn(username, password) {
    if (usuarioExistente(username, password)) {
        alert(`Bienvenido a tu cuenta ${username} 😎!`);
        console.log(usersTimeline);
    } else {
        console.log('😪 Uppss... usuario o contraseña incorrectos!');
    }
}



let username = prompt('Cual es tu nombre?');
username = username[0].toUpperCase() + username.substring(1);

console.log(username);
let passwd = prompt('Cual es tu contraseña?');

signIn(username, passwd);