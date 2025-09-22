<?php 

    // if simple
    $edad = 18;

    // if ($edad >= 18) {
    //     echo "Mayor de edad";
    // } else {
    //     echo "Menor de edad";
    // }

    // Otra forma de representar
     if ($edad >= 18) 
        echo "Mayor de edad";
     else 
        echo "Menor de edad";

    echo "\n";
    
    // if compuesto
    $temp = 15;

    if ($temp >= 25) {
        echo "Calor";
    }elseif ($temp >= 12 and $temp <= 25) {
        echo "templado";
    }else {
        echo "Frio";
    }
    
    echo "\n";
    
    // switch

    echo "1. Suma \n";
    echo "2. Resta \n";
    echo "3. Multiplicacion \n";
    echo "4. Division \n";

    echo "\n";
    

    $operacion = 3;

    switch ($operacion) {
        case 1:
            echo "Operacion: Sumar";
            break;
        case 2:
            echo "Operacion: Restar";
            break;
        case 3:
            echo "Operacion: Multiplicar";
            break;
        case 4:
            echo "Operacion: Dividir";
            break;
        
        default:
            echo "Opcion invalida";
            break;
    }



?>