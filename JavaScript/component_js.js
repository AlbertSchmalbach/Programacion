// Array de elementos
const items = ["react", "javascript", "git"];

// Crear contenedor
const container = document.createElement("div");
const list = document.createElement("ul");

// Recorrer el array y crear elementos
items.forEach(item => {
  const listItem = document.createElement("li");
  listItem.textContent = item;
  list.appendChild(listItem);
});

// Añadir la lista al contenedor
container.appendChild(list);

// Añadir el contenedor al DOM
document.body.appendChild(container);