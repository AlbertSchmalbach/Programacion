<?php 

$edad = 15;

if ($edad >= 18) {
    echo "Eres mayor de edad\n";
} else {
    echo "Eres menor de edad\n";
}

$nota = 9.8;

if ($nota >= 9.5) {
    echo "Excelente\n";
} elseif ($nota>=7.0 && $nota<9.5) {
    echo "Buena\n";
}else {
    echo "Reprabado\n";
}

$dia = "Domingo";

switch ($dia) {
    case 'Lunes':
        echo "Incio de semana";
        break;
    case 'Miercoles':
        echo "mediados de semana";
        break;
    case 'Domingo':
        echo "Fin de semana";
        break;

    default:
        echo "Dia normal";
        break;
}





?>