<?php 

// Comentario de una línea --- Algoritmo Enrique Zambrano

# Otro comentario de una línea 

/* 
Comentario de múltiples líneas  
que abarca varias líneas 
*/ 

// Definir constantes 

define("PI", 3.14); 

class MyMath { 
    const E = 2.71; 
} 

// Declaración de variables 
$number = 10; // entero 
$text = "ten"; // cadena 
$isTrue = true; // booleano 
$price = 19.99; // flotante 

// Arreglo 
$colors = ["red", "green", "blue"]; 

// Objeto 
class Car { 
    public $make; 
    public $model; 
    public $year; 
    public function __construct($make, $model, $year) { 
        $this->make = $make; 
        $this->model = $model; 
        $this->year = $year; 
    } 
    public function getCarInfo() { 
        return $this->year . ' ' . $this->make . ' ' . $this->model; 
    } 
} 

$myCar = new Car("Toyota", "Corolla", 2020); 
 
// Función 
function sum(int $a, int $b): int { 
    return $a + $b; 
} 

// Estructuras de control 
for ($i = 0; $i < 10; $i++) { 
    if ($i == 5) { 
        break;  // Salir del bucle cuando $i es 5 
    } 
    echo $i; 
} 

switch ($number) { 
    case 10: 
        echo "Number is ten"; 
        break; 
    case 20: 
        echo "Number is twenty"; 
        break; 
    default: 
        echo "Number is neither ten nor twenty"; 
} 

// Manejo de excepciones 
function divide($a, $b) { 
    if ($b == 0) { 
        throw new Exception("Division by zero"); 
    } 
    return $a / $b; 
} 

try { 
    echo divide(10, 0); 
} catch (Exception $e) { 
    echo 'Caught exception: ', $e->getMessage(), "\n"; 
} 

// Impresión de datos 
echo "Hello, World!"; 
echo "Value of PI: " . PI; 
echo "Value of E: " . MyMath::E; 
echo $myCar->getCarInfo(); 
?> 