const promise = new Promise((resolve, reject) => {
    setTimeout(() => {
        let validation = true;
        if (validation) {
            resolve("Operacion exitosa 😎");
        } else {
            reject("La operacion fallo 😫");
        }
    }, 2000);
});

promise
    .then((success) => {
        console.log(success);
    })
    .catch((err) => {
        console.error(err);
    });