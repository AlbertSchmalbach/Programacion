<?php 

// Declarando variables
$nombre="Luz Saray";
$edad = 22;
$activo = true;

echo "Nombre: $nombre\n";
echo "Edad: $edad\n";
echo "Estado: $activo\n";

// tipos de datos
$curso = "PHP"; //String
$precio = 199.99; // float
$lecciones = 30; //integer
$disponible = true; //boolean
$vacio = null; //null

echo gettype($precio);

// Operadores

// aritmeticos
$a = 10;
$b = 5;

echo $a + $b;
echo $a - $b;
echo $a * $b;
echo $a / $b;
echo $a % $b;

// Asignacion
$x = 5;
$x += 3;
$x *= 2;

// comparacion
var_dump(10 == "10");
var_dump(10 === "10");
var_dump(5 > 3);

// ejemplo practico
$producto = "Laptop";
$precio = 1540000;
$descuento = 0.10;

$precioFinal = $precio - ($precio * $descuento);

echo "El precio de la $producto es de $$precioFinal\n";

//  Ejercicios Día 2

// Crea un script que defina dos números y muestre la suma, resta, multiplicación, división y módulo.
$num1 = 20;
$num2 = 15;

echo "El resultado de la suma es " . ($num1 + $num2) . "\n";
echo "El resultado de la resta es " . ($num1 - $num2) . "\n";
echo "El resultado de la multiplicacion es " . ($num1 * $num2) . "\n";
echo "El resultado de la division es " . ($num1 / $num2) . "\n";
echo "El resultado del modulo es " . ($num1 % $num2) . "\n";

// De Celsius a Fahrenheit F = (C × 9/5) + 32
$c = 30;

$f = ($c * (9/5)) + 32;

echo "La conversion de $c grados celcius a farenheit es de $f\n";

// Si una persona tiene X años, calcula su edad en meses, semanas y días.
$x = 20;

$edad_meses = $x * 12;
$edad_semanas = $x * 52.143;
$edad_dias = $x * 365;

echo "La edad de $x años en meses corresponde a $edad_meses\n";
echo "La edad de $x años en semanas corresponde a $edad_semanas\n";
echo "La edad de $x años en dias corresponde a $edad_dias\n";


?>