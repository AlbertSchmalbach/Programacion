const form = document.querySelector('#myForm');
// const name = document.querySelector('#name');
// const email =document.querySelector('#email');
// const submit = document.querySelector('button');


form.addEventListener("submit", (event) => {
    event.preventDefault();
    const name = form.elements['name'].value;
    console.log(name);
});
