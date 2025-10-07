<?php

    // $edades = [12, 20, 40];
    $edades = array(25, 15, 30);

    echo "Edad: ". $edades[1];

    echo "\n";


    // Array asociativo

    $laptop = array(
        "Lenovo" => 2130000,
        "HP" => 2050000,
        "Dell" => 2250000,
        "Mac" => 2500000,
    );

    echo "El precio de la laptop es $ {$laptop['Dell']} pesos";


    // Array multidimensionales
    $programador = array(
        "programador1" => array(
            "nombre" => "Alberto",
            "lenguajes" => ["Python", "Java", "Javascript", "PHP", "C++", "Html", "CSS", "SQL"]
            ),
        "programador2" => array(
            "nombre" => "Luz Saray",
            "lenguajes" => ["Python", "Javascript", "PHP","Html", "CSS"]
        ),
        "programador3" => array(
            "nombre" => "Said",
            "lenguajes" => ["Javascript", "PHP","Html", "CSS"]
        ),
    );

    echo "\n";

echo "Nombre del programador: {$programador['programador2']['nombre']}\n";
echo "Lenguajes: {$programador['programador2']['lenguajes'][1]}\n";


// Manipulacion de arreglos
$chicas = array(
    "Luz Saray",
    "Nazly",
    "Maria Fernanda",
    "Yissel",
);

// Count()
echo count($chicas);

// arry_push()
array_push($chicas, "Misuris Paola");
echo "\n";
// var_dump($chicas);

// is_array()
echo is_array($chicas);
echo "\n";
var_dump(is_array($chicas));

$lenguajes = "Python, PHP, Java, Javascript";

$lenguajes_array = explode(",", $lenguajes);
print_r($lenguajes_array);

// print("Hola mundo");

// implode
$chicas_string = implode(",", $chicas);
echo $chicas_string;

