<?php

    $saludo = "Hola";

    // heredoc
    echo <<<frase
        $saludo
        solo se que nada se
        frase;

    // Nowdoc
    echo <<<'frase'
        $saludo
        Otra frase
        frase;