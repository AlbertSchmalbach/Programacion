<?php

    $nombre = "Luz Saray";

    // $primerNombre = substr($nombre,0,3);
    // $segundoNombre = substr($nombre, 4, strlen($nombre)-1);
    $segundoNombre = "Saray";

    $posicion = strpos($nombre, $segundoNombre);

    echo $posicion;

    $extraccion = substr($nombre, $posicion);

    echo $extraccion;



    // echo $primerNombre;
    // echo "\n";
    // echo $segundoNombre;