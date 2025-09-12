<?php  

    $a = 10;
    $b = 4.528;
    $c = "25";

    var_dump($a);
    var_dump($b);
    var_dump($c);

    // is_int()
    var_dump(is_int($a));

    // is_float()
    var_dump(is_float($b));

    // is_finite()
    $x = 1.9e411;
    var_dump(is_infinite($x));

    // is_nan()
    $y = "12";
    var_dump(is_nan($y));

    // is_numeric()
    var_dump(is_numeric($y));

    // Conversión de cadenas y flotantes a enteros en PHP

    // Cast float to int
    $int_cast = (int)$b;
    echo $int_cast;

    echo "<br>";

    // Cast string to int
    $x = "23465.768";
    $int_cast = (int)$x;
    echo $int_cast;



?>