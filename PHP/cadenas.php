<?php

    $name = "Albert";
    $text = "Python es mi lenguaje de programacion favorito";
    echo "Hello $name\n";
    echo 'Hello $name'."\n";

    // Longitud
    echo strlen("Hola mundo");
    echo "\n";
    // Contar palabras
    echo str_word_count("Hola mundo");
    echo "\n";
    // Buscar posicion de palabra en oracion
    echo strpos("Hello world!", "world");
    echo "\n";
    // mayusc
    echo strtoupper($name);
    echo "\n";
    // minusc
    echo strtolower($name);
    echo "\n";
    // remplazar
    echo str_replace("Python", "JavaScript", $text);
    echo "\n";
    // Invertir cadena
    echo strrev($text);
    echo "\n";
    // Eliminar espacio
    echo trim(" Hello name");
    echo "\n";
    // Cadena en matrid
    print_r (explode(" ", $text));
    // Concatenación de cadenas (.)
    $x = "Hello";
    $y = "World";

    $z = $x ." ". $y;
    $n = "$x $y";

    echo $z;
    echo "\n";
    echo $n;
    echo "\n";

    // Rebanar
    echo substr($text, 13, 24);
?>