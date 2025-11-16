const h1 = document.getElementById('title');
const input1 = document.querySelector('#cal1');
const input2 = document.querySelector('#cal2');
const btn_calcular = document.querySelector('#btn_calcular');
const btn_clear = document.getElementById('btn_clear');
const res = document.querySelector('#result');
const DivImage = document.querySelector('.image');


btn_calcular.addEventListener('click', (e) => {
    e.preventDefault();
    const result = parseInt(input1.value) + parseInt(input2.value);
    res.innerHTML = result;

    input1.value = '';
    input2.value = '';
});

btn_clear.addEventListener('click', (e) => {
    e.preventDefault();
    res.innerHTML = 0;
})

const img = document.createElement('img');
img.src = './image/img2.png';

DivImage.appendChild(img);