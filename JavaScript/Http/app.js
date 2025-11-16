const url = "https://jsonplaceholder.typicode.com/posts";
const form = document.querySelector('#new-post form');
const listElement = document.querySelector('.posts');
const fetchButton = document.querySelector('#available-posts button');
const postList = document.getElementById('posts-container');


// fetch(url)
// .then(res => res.json())
// .then(data => console.log(data))

/**
 * Función para enviar una solicitud HTTP genérica
 * @param {string} method - Método HTTP (GET, POST, PUT, DELETE, etc.)
 * @param {string} url - URL del endpoint
 * @param {object} data - Datos a enviar en el body (opcional para GET)
 * @returns {Promise} - Promesa que resuelve con los datos JSON de la respuesta
 */
function sendHTTPRequest(method, url, data) {
    return fetch(url, {
        method: method,                                    // Especifica el método HTTP
        body: JSON.stringify(data),                       // Convierte los datos a JSON string
        headers: {
            'Content-Type': 'application/json'            // Define el tipo de contenido como JSON
        }
    })
    .then(res => {
        return res.json()                                 // Convierte la respuesta a objeto JSON
    });
}

/**
 * Función asincrónica para obtener posts de la API y mostrarlos en el DOM
 * Utiliza await para esperar la respuesta de sendHTTPRequest
 */
async function fetchPosts() {
    // Realiza una solicitud GET a la API y espera la respuesta
    const resData = await sendHTTPRequest("GET", url);
    console.log(resData);                                 // Imprime en consola los datos recibidos
    const listOfPosts = resData;                          // Almacena los posts en una variable

    // Itera sobre cada post recibido de la API
    for (const post of listOfPosts) {
        // Crea un elemento article para cada post
        const postContainer = document.createElement('article');
        postContainer.id = post.id;                       // Asigna el ID del post como atributo id del article
        postContainer.classList.add('post-item');         // Añade la clase CSS 'post-item'

        // Crea un elemento h2 para el título del post
        const title = document.createElement('h2');
        title.textContent = post.title;                   // Asigna el título del post al elemento

        // Crea un elemento p para el contenido del post
        const body = document.createElement('p');
        body.textContent = post.body;                     // Asigna el cuerpo del post al elemento

        // Crea un botón para eliminar contenido
        const button = document.createElement('button');
        button.textContent = 'DELETE Content';            // Texto del botón

        // Añade todos los elementos creados al contenedor del post
        postContainer.append(title);                      // Añade el título
        postContainer.append(body);                       // Añade el cuerpo
        postContainer.append(button);                     // Añade el botón de eliminación

        // Añade el contenedor completo del post al elemento lista en el DOM
        listElement.append(postContainer);
    }
}

// Agrega un event listener al botón para ejecutar fetchPosts cuando se haga click
fetchButton.addEventListener('click', fetchPosts);

async function createPosts(title, content) {
    const userID = Math.floor(Math.random() * 100);
    console.log(userID)
    const post = {
        title: title,
        body: content,
        userID: userID
    }; 

    sendHTTPRequest("POST", url, post)
}

form.addEventListener("submit", (e) => {
    e.preventDefault();
    const title = e.currentTarget.querySelector('#title').value;
    const content = e.currentTarget.querySelector('#content').value;

    createPosts(title, content);
});

postList.addEventListener('click', (e) => {
    if (e.target.tagName === "BUTTON") {
        const postId = e.target.closest('article').id;
        console.log(postId);
        sendHTTPRequest('DELETE', `${url}/${postId}`);
    } else {
        
    }
})