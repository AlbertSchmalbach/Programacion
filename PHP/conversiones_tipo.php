<?php 

    $nombre = "Luz Saray";
    $edad = 23;
    $esMujer = true;
    $estatura = 1.56;

    // Obtener tipo
    echo gettype($nombre). "\n";
    echo gettype($edad). "\n";
    echo gettype($esMujer). "\n";
    echo gettype($estatura). "\n";

    // Convertir tipo (Automatica y manual)
    $num1 = "12.5";
    $num2 = 30;
    $result = $num1 + $num2;

    echo "Resultado de la suma : " . intval( $result ) ."\n";

    // Otra forma
    $numero = "12";
    echo gettype($numero). "\n";
    $cvNumero = (int) $num1;
    echo gettype($cvNumero). "\n";


?>