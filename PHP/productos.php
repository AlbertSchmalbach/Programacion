<?php

    $productos = array(
        array(
            "Nombre" => "Manzana",
            "Precio" => 1500,
            "otros" => array(
                "color" => "roja",
                "tipo" => "rosaceas"
            ),
        ),

        array(
            "Nombre" => "Sandia",
            "Precio" => 12000,
            "otros" => array(
                "color" => "Verde",
                "tipo" => "cucurbitácea"
            ),
        ),

        array(
            "Nombre" => "Banana",
            "Precio" => 500,
            "otros" => array(
                "color" => "Amarillo",
                "tipo" => "baya"
            ),
        )
    );

    echo "Mi fruta favorita es la {$productos[2]['Nombre']},tiene un color {$productos[2]['otros']['color']} y 
        cuesta {$productos[2]['Precio']} pesos.";