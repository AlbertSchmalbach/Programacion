<?php

    // for( $i = 0; $i < 10; $i++ ){
    //     echo "Linea: $i \n";
    // }

    $frutas = array(
        "Pera"=> 1200,
        "Manzana"=> 1500,
        "Melon"=> 7200,
        "Sandia"=> 12000,
        "Piña"=> 1600
    );


// foreach($frutas as $fruta => $precio) {
//     echo "el fruto $fruta cuesta $$precio \n";
// }

foreach($frutas as $fruta => $precio) {
    
    if ($fruta == "Melon") {
        echo "No apatece el $fruta \n";
        continue;
    }

    echo "Quiero $fruta\n";
}

// foreach($frutas as $fruta => $precio) {
//     echo "Fruta: $fruta \n";
//     if ($fruta == "Sandia") {
//         echo "La $fruta es mi fruta favorita.\n";
//         break;
//     }
// }


?>