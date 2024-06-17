<?php 
// Declaración de variables 

$entero = 10; // Entero 

$flotante = 3.14; // Flotante 

$cadena = "Hola"; // Cadena de texto 

$booleano = true; // Booleano 

// Arreglo 

$arreglo = [1, 2, 3]; 

// Objeto y Clase 

class MiClase { 

    public $propiedad = "valor"; 

    public function metodo($param) { 

        return $param * 2; 

    } 

} 

$objeto = new MiClase(); 

echo $objeto->metodo(5) . "\n"; 

// Operadores aritméticos y de asignación 

$suma = $entero + 5; 

$resta = $entero - 3; 

$multiplicacion = $entero * 2; 

$division = $entero / 2; 

$modulo = $entero % 3; 

$entero += 2; 

// Operadores lógicos 

$and = $booleano && false; 

$or = $booleano || false; 

$not = !$booleano; 

// Estructura de control: if 

if ($booleano) { 

    echo "Es verdadero\n"; 

} else { 

    echo "Es falso\n"; 

} 

// Bucle for 

for ($i = 0; $i < 3; $i++) { 

    echo $arreglo[$i] . "\n"; 

} 

// Función 

function suma($a, $b) { 

    return $a + $b; 

} 

echo suma(2, 3) . "\n"; 

// Manejo de excepciones 

try { 

    if ($entero < 0) { 

        throw new Exception("Número negativo"); 

    } 

} catch (Exception $e) { 

    echo "Error: " . $e->getMessage() . "\n"; 

} 
?> 