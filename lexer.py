import ply.lex as lex
import datetime
import os
from ply.ctokens import t_ARROW

# Definición de los tokens
tokens = [
    # inicio - Alejandro Barrera
    'VARIABLE',
    'INTEGER',
    'FLOAT',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MOD',
    'EXP',
    'STRING',
    'COMMENT',
    'ARROW',
    'COMMA',
    'IDENTIFIER',
    'SET',
    'DOLLAR'
    # fin - Alejandro Barrera
]

# Definición de las palabras reservadas
reserved = {
    # inicio - Enrique Zambrano
    'if': 'IF', 
    'else': 'ELSE',
    'array' : 'ARRAY',
    'elseif': 'ELSEIF', 
    'while': 'WHILE', 
    'do': 'DO',
    'for': 'FOR', 
    'foreach': 'FOREACH', 
    'switch': 'SWITCH', 
    'case': 'CASE', 
    'default': 'DEFAULT',
    'break': 'BREAK', 
    'continue': 'CONTINUE', 
    'return': 'RETURN', 
    'function': 'FUNCTION',
    'class': 'CLASS', 
    'extends': 'EXTENDS', 
    'implements': 'IMPLEMENTS', 
    'public': 'PUBLIC',
    'protected': 'PROTECTED', 
    'private': 'PRIVATE', 
    'static': 'STATIC', 
    'const': 'CONST',
    'var': 'VAR', 
    'new': 'NEW', 
    'try': 'TRY', 
    'catch': 'CATCH', 
    'finally': 'FINALLY', 
    'throw': 'THROW',
    'break' : 'BREAK'
    # fin - Enrique Zambrano
}

tokens += list(reserved.values())

tokens += [
    #inicio - Pratt Garcia
    'NEWLINE',
    'AND',
    'OR',
    'NOT',
    'EQ',
    'IDENTICAL',
    'NE',
    'NOT_IDENTICAL',
    'LT',
    'GT',
    'LE',
    'GE',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'LBRACKET',
    'RBRACKET',
    'SEMI',
    'ERROR',
    'CONSTRUCT'
    #Fin - Pratt Garcia
]

# Definición de los patrones de los tokens

#Inicio - Pratt Garcia
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_EQ = r'=='
t_IDENTICAL = r'==='
t_NE = r'!='
t_NOT_IDENTICAL = r'!=='
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_SEMI = r';'
t_CONSTRUCT = r'__construct'


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

t_ignore = ' \t'

#Fin - Pratt Garcia

# Definición de los patrones de los tokens

# Inicio - Alejandro Barrera
t_SET     = r'='
t_DOLLAR  = r'\$'
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_MOD     = r'%'
t_ARROW   = r'=>'
t_COMMA   = r','

def t_VARIABLE(t):
    r'$[_a-zA-Z][_a-zA-Z0-9]\w*'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t

def t_FLOAT(t):
    r'\d+\.(\d+)?'
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# fin - Alejandro Barrera

# Inicio - Pratt Garcia
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

# Fin - Pratt Garcia

# Inicio - Enrique Zabrano
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_COMMENT(t):
    r'//.*|/\*[^*]*\*+(?:[^/*][^*]*\*+)*/|\#.*'
    pass  # Ignorar comentarios

def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.type = 'STRING'
    return t

# fin - Enrique Zambrano

# Regla para manejar errores
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

# Función para realizar pruebas y generar logs
def test_lexer(data, username):
    lexer.input(data)
    log_folder = "logs"
    os.makedirs(log_folder, exist_ok=True)
    current_time = datetime.datetime.now().strftime("%d%m%Y-%Hh%M")
    log_filename = f"lexico-{username}-{current_time}.txt"
    log_path = os.path.join(log_folder, log_filename)

    with open(log_path, "w") as log_file:
        while True:
            tok = lexer.token()
            if not tok:
                break
            log_file.write(f"{tok.type}: {tok.value} (line {tok.lineno})\n")
            print(f"{tok.type}: {tok.value} (line {tok.lineno})")

#Prueba de Lexer con algoritmo de Enrique Zambrano
#Inicio - Enrique Zambrano
data1 = '''
$var1 = 10;
$var2 = $var1 + 20;
'''

#test_lexer(data1, "EZambranoFx")

data2 =    '''
<?php
// Factorial function
function factorial($n) {
    if ($n == 0) {
        return 1;
    }
    return $n * factorial($n - 1);
}

$number = 5;
echo "Factorial of $number is " . factorial($number);
?>
'''
#test_lexer(data2, "EZambranoFx")
#Fin - Enrique Zambrano

#Prueba de Lexer con algoritmo de Pratt Garcia
#Inicio - Pratt Garcia
AlgoritmoPrattGarcia = '''
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
'''
#test_lexer(AlgoritmoPrattGarcia, "PrattGarcia")

#Final - Pratt Garcia

#Inicio - Alejandro Barrera
AlgoritmoAlejandroBarrera = '''
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
'''
#test_lexer(AlgoritmoAlejandroBarrera, "AlejandroBarrera")
#Final - Alejandro Barrera