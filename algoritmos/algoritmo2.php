<?php 

// Comentario de una línea --- Algoritmo Alejandro Barrera

// Comentario de una línea

/*
 Comentario de múltiples líneas
 */

// Declaración de variables
$entero = 32; // Entero
$flotante = 6.28; // Flotante
$cadena = "Hola Mundo"; // Cadena de texto
$booleano = false; // Booleano

// Arreglo
$arreglo = [7, “i”, [1, 2]];

// Objeto y Clase
class Clase {
    public $propiedad = "valor";
    public function método($parametro) {
        echo $parametro;
        return;
    }
}
$instancia = new Clase ();
echo $instancia -> método(“Hola”). "\n";

// Operadores aritméticos y de asignación
$suma = $entero + 5;
$resta = $entero - 3;
$multiplicación = $entero * 2;
$división = $entero / 2;
$modulo = $entero % 3;
$entero += 2;

// Operadores lógicos
$and = $booleano && false;
$or = $booleano || false;
$not = !$booleano;

// Estructura de control: if
if ($entero >= 10) {
    echo "Mayor que 10\n";
} else if ($entero < 5) {
    Echo "Entre 1 y 5\n";  
} else {
    echo "Entre 10 y 5\n";
}

// Bucle while
$i = 1;
while ($i <= 10) {
    echo $i++;
}

// Función
function multiplicación($a, $b) {
    return $a * $b;
}

echo suma (2, 3). "\n";
?> 