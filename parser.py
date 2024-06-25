import ply.yacc as yacc
from lexer import tokens
import datetime
import os


# Inicio - Enrique Zambrano

# Estructura de Datos: Declaracion de objetos
def p_object_declaration(p):
    '''object_declaration : VAR VARIABLE EQ NEW CLASS LPAREN RPAREN SEMI'''

def p_statement(p):
    '''statement : print_statement
                 | input_statement
                 | expression_statement
                 | assignment_statement
                 | condition
                 | data_structure_statement
                 | function_statement
                 | class_statement
                 | ifStatement
                 | array'''
    p[0] = p[1]
    
def p_assignment_statement(p):
    '''assignment_statement : VARIABLE EQ expression SEMI'''
    p[0] = ('assign', p[1], p[3])
    
def p_data_structure_statement(p):
    '''data_structure_statement : array
                                | class_statement'''
    p[0] = p[1]
    
def p_class_statement(p):
    '''class_statement : CLASS IDENTIFIER LBRACE class_body RBRACE'''
    p[0] = ('class', p[2], p[4])

def p_function_statement(p):
    '''function_statement : FUNCTION IDENTIFIER LPAREN parameter_list RPAREN LBRACE statement_list RBRACE'''
    p[0] = ('function', p[2], p[4], p[7])

# Estructura de Control: While
def p_while_statement(p):
    '''while_statement : WHILE LPAREN expression RPAREN statement'''


# Funcion: Funcion Variable
def p_function_variable(p):
    '''function_variable : FUNCTION VARIABLE LPAREN RPAREN LBRACE statements RBRACE'''


# Impresion
def p_print_statement(p):
    '''print_statement : ECHO LPAREN expression_list RPAREN SEMI
                       | ECHO expression_list SEMI'''


# Solicitud de Datos
def p_input_statement(p):
    '''input_statement : VARIABLE EQ READLINE LPAREN RPAREN SEMI
                       | empty'''


# Expresiones Aritmeticas
def p_expression_statement(p):
    '''expression_statement : expression SEMI'''


# Fin - Enrique Zambrano

# Inicio - Alejandro Barrera

# Estructura de Datos: Declaración de arreglos
def p_array(p):
    '''array : ARRAY LPAREN arrayArg RPAREN SEMI'''


def p_arrayArg(p):
    '''arrayArg : index ARROW value
                | index ARROW value arrayArg
                | index ARROW value COMMA arrayArg'''


# Estructura de Control: if y else
def p_ifStatement(p):
    '''ifStatement : IF LPAREN condition RPAREN LBRACE statements RBRACE SEMI
                    | IF LPAREN condition RPAREN LBRACE statements RBRACE elseStatement'''


def p_elseStatement(p):
    '''elseStatement : ELSE LBRACE statements RBRACE SEMI'''


def p_condition(p):
    '''condition : expression comparison_operator expression
                 | condition logical_operator condition'''
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3])
    else:
        p[0] = (p[2], p[1], p[3])
        

def p_index(p):
    '''index : INTEGER
            | STRING'''


#Función: Funciones de flecha.
def p_arrowFunction(p):
    '''arrowFunction : FUNCTION LPAREN VARIABLE RPAREN ARROW expression SEMI
                    | FUNCTION LPAREN VARIABLE RPAREN ARROW arrowFunction'''



def p_comparison_operator(p):
    '''comparison_operator : LT
                            | GT
                            | LE
                            | GE
                            | EQ
                            | NE'''


def p_value(p):
    '''value : VARIABLE
            | INTEGER
            | FLOAT
            | expression_statement'''



# Fin - Alejandro Barrera

# Inicio - Pratt Garcia
def p_expression(p):
    '''expression : term
                  | expression PLUS term
                  | expression MINUS term
                  | expression TIMES term
                  | expression DIVIDE term'''


def p_expression_list(p):
    '''expression_list : expression_list COMMA expression
                       | expression'''


def p_empty(p):
    '''empty :'''
    pass


def p_statements(p):
    '''statements : statements statement
                  | statement
                  | empty'''


def p_compound_statement(p):
    '''compound_statement : LBRACE statements RBRACE'''


def p_class_declaration(p):
    '''class_declaration : CLASS IDENTIFIER LBRACE class_body RBRACE'''


def p_class_body(p):
    '''class_body : class_member_list'''


def p_class_member_list(p):
    '''class_member_list : class_member_list class_member
                         | empty'''


def p_class_member(p):
    '''class_member : property_declaration
                    | method_declaration
                    | constructor_declaration'''


def p_property_declaration(p):
    '''property_declaration : visibility VARIABLE SEMI'''


def p_method_declaration(p):
    '''method_declaration : visibility FUNCTION IDENTIFIER LPAREN parameter_list RPAREN LBRACE statement_list RBRACE'''


def p_constructor_declaration(p):
    '''constructor_declaration : visibility FUNCTION CONSTRUCT LPAREN parameter_list RPAREN LBRACE statement_list RBRACE'''


def p_visibility(p):
    '''visibility : PUBLIC
                  | PROTECTED
                  | PRIVATE'''


def p_parameter_list(p):
    '''parameter_list : parameter_list COMMA parameter
                      | empty'''


def p_parameter(p):
    '''parameter : TYPE VARIABLE
                 | VARIABLE'''


def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''


# Definicion del elseif
def p_elseif_statement(p):
    '''elseif_statement : ELSEIF LPAREN expression RPAREN statement'''


# Funciones anonimas
def p_anonymous_function(p):
    '''anonymous_function : FUNCTION LPAREN parameter_list RPAREN use_clause_opt LBRACE statement_list RBRACE'''


def p_use_clause_opt(p):
    '''use_clause_opt : USE LPAREN variable_list RPAREN
                      | empty'''


def p_variable_list(p):
    '''variable_list : variable_list COMMA VARIABLE
                     | VARIABLE'''


def p_logical_operator(p):
    '''logical_operator : AND
                        | OR'''


# Definición de Variables (todos los tipos) y almacenamiento de resultados de expresiones/condicionales
def p_variable_declaration(p):
    '''variable_declaration : VARIABLE EQ expression SEMI
                            | VARIABLE EQ condition SEMI'''


def p_term(p):
    '''term : INTEGER
            | STRING
            | VARIABLE
            | LPAREN expression RPAREN'''


# Declarar Estructuras de Datos
def p_array_declaration(p):
    '''array_declaration : VARIABLE EQ ARRAY LPAREN array_elements RPAREN SEMI'''


def p_array_elements(p):
    '''array_elements : array_elements COMMA array_element
                      | array_element
                      | empty'''


def p_array_element(p):
    '''array_element : expression
                     | expression ARROW expression'''


# Fin - Pratt Garcia

parser = yacc.yacc()


def test_parser(data, username):
    result = parser.parse(data)
    log_folder = "logs"
    os.makedirs(log_folder, exist_ok=True)
    current_time = datetime.datetime.now().strftime("%d%m%Y-%Hh%M")
    filename = f"Sintactico-{username}-{current_time}.txt"
    with open(os.path.join(log_folder, filename), 'w') as log_file:
        log_file.write(str(result))
    return result

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
test_parser(AlgoritmoAlejandroBarrera, "AlejandroBarrera")
#Final - Alejandro Barrera

