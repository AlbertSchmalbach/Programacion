// Calcula el perímetro y el área de una circunferencia dado su radio

// Retorna un objeto con las propiedades { perimetro, area }
function areaPerimetroCircunferencia(r) {
    let perimetro = 2 * (Math.PI) * r; 
    let area = Math.PI * (r ** 2); 
    
    return { perimetro, area };
}


// Ejemplo de uso
let radio = 12;
let resultado = areaPerimetroCircunferencia(radio);
console.log()

// Mostramos los resultados en consola
console.log('Perimetro:', (resultado.perimetro).toFixed(2));
console.log('Área:', (resultado.area).toFixed(2));