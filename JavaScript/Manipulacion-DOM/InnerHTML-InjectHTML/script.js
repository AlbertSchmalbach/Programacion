const contentArea = document.getElementById('contentArea');
const listArea = document.getElementById('listArea');

contentArea.innerHTML = "<p>Este es un nuevo parrafo dentro del contenedor</p>";
contentArea.innerHTML+= "Otro parrafo añadido al contenedor";

listArea.insertAdjacentHTML('beforeend',
    `<li>Item 5</li>
     <li>Item 6</li>
     <li>Item 7</li>`);