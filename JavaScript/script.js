// Obtenemos los elementos del HTML
const tareaInput = document.getElementById('tareaInput');
const agregarBtn = document.getElementById('agregarBtn');
const listaTareas = document.getElementById('listaTareas');

// Cargar tareas guardadas al iniciar
document.addEventListener('DOMContentLoaded', cargarTareas);

// Escucha el clic del botón
agregarBtn.addEventListener('click', () => {
    const texto = tareaInput.value.trim();
    if (texto === '') return alert('Escribe una tarea');

    // Crear nuevo elemento <li>
    const li = document.createElement('li');
    li.textContent = texto;


    // Eliminar tarea al hacer clic sobre ella
    // li.addEventListener('click', () => {
    //     li.remove();
    // });


    // Agregar la tarea a la lista
    // listaTareas.appendChild(li);

    agregarTarea(texto);
    guardarTareas(); // actualizar localStorage

    // Limpiar el input
    tareaInput.value = '';

});

// Función para agregar tarea al DOM
function agregarTarea(texto) {
    const li = document.createElement('li');
    li.textContent = texto;

     // Eliminar tarea al hacer clic
    li.addEventListener('click', () => {
        li.remove();
        guardarTareas();
    });

    listaTareas.appendChild(li);
}

// Función para guardar tareas en localStorage
function guardarTareas() {
    const tareas = [];
    listaTareas.querySelectorAll('li').forEach(li => tareas.push(li.textContent));
    localStorage.setItem('tareas', JSON.stringify(tareas));
}

function cargarTareas() {
    const tareasGuardadas = JSON.parse(localStorage.getItem('tareas')) || [];
    tareasGuardadas.forEach(t => agregarTarea(t));
}