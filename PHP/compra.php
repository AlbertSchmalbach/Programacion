<?php

    /*
        DESCUENTO POR VALOR DE LA COMPRA:
        Si es mayor 500 mil, 30% de descuento
        Si es mayor 200 mil y menor o igual 500 mil, 25% de descuento
        Si es mayor 100 mil y menor o igual 200 mil, 15% de descuento
        si es menor o igual a 100 mil 10%;

    */

$monto_inicial = readline("Cual es el monto inicial de tu compra: ");
$monto_inicial= (double) $monto_inicial;
$por_descuento = 0;

if ($monto_inicial > 500000) {
    $por_descuento = 30;
    $vlrdesc = ($monto_inicial * $por_descuento)/100;
    $monto_final = $monto_inicial - $vlrdesc;
} elseif($monto_inicial > 200000 and $monto_inicial <= 500000) {
    $por_descuento = 20;
    $vlrdesc = ($monto_inicial * $por_descuento)/100;
    $monto_final = $monto_inicial -$vlrdesc;
}elseif($monto_inicial > 100000 and $monto_inicial <= 200000) {
    $por_descuento = 15;
    $vlrdesc = ($monto_inicial * $por_descuento)/100;
    $monto_final = $monto_inicial - $vlrdesc;
}else{
    $por_descuento = 10;
    $vlrdesc = ($monto_inicial * $por_descuento)/100;
    $monto_final = $monto_inicial - $vlrdesc;
}

echo "Tu compra en principio es de $$monto_inicial pesos, pero con el $por_descuento% queda en $$monto_final pesos";