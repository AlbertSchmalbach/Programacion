const section = document.querySelector('section');

const p = document.createElement('p');
p.textContent = "Este parrafo cue creado con JS";
section.append(p);

const remplazoP = document.createElement('p');
remplazoP.textContent = "Estoy reemplazando a otro parrafo";

const h2 = document.createElement('h2');
h2.textContent = 'Primer subtitulo';
section.after(h2);

section.removeChild(section.children[1]);

const selectP = section.children[1];
const cloneP = selectP.cloneNode(true);
section.appendChild(cloneP);
cloneP.textContent = "Este parrafo es el clone modificado";

const selectPremplazar = section.children[2];
selectPremplazar.replaceWith(remplazoP);
