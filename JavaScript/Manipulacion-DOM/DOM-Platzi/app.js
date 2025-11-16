const title = document.getElementById("app-title");
const section = document.querySelector("section");
const btnTogleMenu = document.querySelector("main button:first-child");
console.dir(title);

const menu = document.querySelector("menu");

const ul = document.querySelector("#parent");

const btn_color = document.querySelector("#btn-color");

// btn_color.setAttribute("onclick", "document.body.style.backgroundColor = '#222'");

btnTogleMenu.addEventListener("click", () => {
    menu.classList.toggle("invisible");
});

btn_color.addEventListener("click", () => {
    document.body.classList.toggle("addBodyBackground");
    title.classList.toggle("app-title-color");
    menu.style.fontSize = "18px";
    ul.classList.toggle("main-menu");

    for (const btn of document.querySelectorAll("button")) {
        btn.classList.toggle("colorFondoBtn");
    }

    for (const p of section.querySelectorAll("p")) {
        p.classList.toggle("styleSection");
    }
});
