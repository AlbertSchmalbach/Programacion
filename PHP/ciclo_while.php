<?php

    $contador = 1;
    $factorial = 1;

    $numero = readline("Ingresa un numero: ");

    while ($contador <= $numero) {
        $factorial *= $contador;
        $contador++;
    }

    echo "El factorial de $numero es: $factorial";

    echo "\n";

     $contrasena = "pass2012";

     do {
        $userPass = readline("Ingresa contraseña: ");
     } while ($userPass != $contrasena);

