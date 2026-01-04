// const listItems = document.querySelectorAll('li');

// listItems.forEach((item)=> {
//     item.addEventListener('click', (event) => {
//         event.target.classList.toggle("hightlight");
//     });
// });

const list = document.querySelector('ul');

list.addEventListener('click', (e) => {
    e.target.closest('li').classList.toggle('hightlight');
});
        