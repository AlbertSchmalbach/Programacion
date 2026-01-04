const container = document.querySelector(".container-img");
const btn = document.querySelector("button");

function ocultarImage() {
    container.classList.add("invisible");
    btn.textContent = "Desocultar";
    btn.removeEventListener('click', ocultarImage);
    btn.addEventListener('click', mostrarImage);
}

function mostrarImage() {
    container.classList.remove("invisible");
    btn.textContent = "Ocultar";
    btn.removeEventListener('click', mostrarImage);
    btn.addEventListener('click', ocultarImage);
}

container.addEventListener("mouseover", () => {
  container.style.backgroundImage = "url(https://lipsum.app/id/50/500x300)";
});

container.addEventListener("mouseout", () => {
  container.style.backgroundImage = "url(https://lipsum.app/id/12/500x300)";
});

btn.addEventListener("click", ocultarImage);



