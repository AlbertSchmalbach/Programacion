<?php

    $correo = "albert2550@hotmail.com";
    $dominio = "hotmail";


    $remplazar_dominio = str_replace($dominio, "gmail", $correo);

    echo $remplazar_dominio;

    $ano = 2025;
    $mes = 10;
    $dia = 24;
    $formato = "%s/%s/%s";

    echo "\n";

    echo sprintf($formato, $ano,$mes, $dia);