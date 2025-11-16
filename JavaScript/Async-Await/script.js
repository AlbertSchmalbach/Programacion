const API_URL = "https://pokeapi.co/api/v2/pokemon";

// Tradicional
// function obtenerData() {

//     fetch(API_URL)
//         .then((res) => {
//             res.json();
//         })
//         .then((data) => {
//             console.log(data)
//         })
//         .catch((err) => {
//             console.error(err);
//         })
// }

// console.log(fetchData())

// Con async y await
async function getData() {
    try {
        let res = await fetch(API_URL);
        let data = await res.json();
        for (dato of data.results) {
            console.log(dato.name);
        }
        return data;
    } catch (error) {
        console.error(error);
        throw error;
    }
}

console.log(getData())

const urls = [
    "https://rickandmortyapi.com/api/character",
    "https://rickandmortyapi.com/api/location",
    "https://rickandmortyapi.com/api/episode"
]

// const fetchNewData = async (res, rej) => {
//     try {
//         for await (const url of urls) {
//             res = await fetch(url);
//             let data = await res.json();
//             for (const e of data.results) {
//                 console.log(e.name);
//             }
//         }
//     } catch (error) {
//         console.error(error)
//     }
// }

// console.log(fetchNewData())