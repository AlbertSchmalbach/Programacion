function calcuclateDiscount(price, percentageDiscount) {
    const discount = (price * percentageDiscount)/100;
    const priceDiscount = price - discount;
    return priceDiscount;
}

const priceOriginal = 56400;
const percentageDiscount = 15;
const priceDiscount = calcuclateDiscount(priceOriginal, percentageDiscount);

console.log('Precio original del producto: $'+ priceOriginal);
console.log('Precio con descuento: $'+ priceDiscount);
console.log(`Obtuviste un ahorro de $${priceOriginal - priceDiscount}`);