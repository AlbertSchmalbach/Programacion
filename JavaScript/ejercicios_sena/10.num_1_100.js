function mostrarNumUnoCienRecursiva(num=1){
    if(num > 100) return;
    console.log(num);
    mostrarNumUnoCienRecursiva(num + 1);
}

mostrarNumUnoCienRecursiva();