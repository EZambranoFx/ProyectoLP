import ply.yacc as yacc
import datetime
import os
from lexer import tokens

# Definición de la gramática

# Definición de la estructura de datos de la gramática
def p_program(p):
    '''program : statement_list'''
    p[0] = p[1]

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    '''statement : print_statement
                 | input_statement
                 | expression_statement
                 | assignment_statement
                 | condition_statement
                 | data_structure_statement
                 | function_statement
                 | class_statement'''
    p[0] = p[1]

def p_print_statement(p):
    '''print_statement : IDENTIFIER LPAREN argument_list RPAREN SEMI'''
    p[0] = ('print', p[3])

def p_input_statement(p):
    '''input_statement : IDENTIFIER LPAREN RPAREN SEMI'''
    p[0] = ('input',)

def p_argument_list(p):
    '''argument_list : expression
                     | argument_list COMMA expression'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_expression_statement(p):
    '''expression_statement : expression SEMI'''
    p[0] = ('expression', p[1])

def p_assignment_statement(p):
    '''assignment_statement : VARIABLE EQ expression SEMI'''
    p[0] = ('assign', p[1], p[3])

def p_condition_statement(p):
    '''condition_statement : IF LPAREN condition RPAREN statement
                           | IF LPAREN condition RPAREN statement ELSE statement'''
    if len(p) == 6:
        p[0] = ('if', p[3], p[5])
    else:
        p[0] = ('if-else', p[3], p[5], p[7])

def p_data_structure_statement(p):
    '''data_structure_statement : array_statement
                                | class_statement'''
    p[0] = p[1]

def p_array_statement(p):
    '''array_statement : VARIABLE EQ LBRACKET argument_list RBRACKET SEMI'''
    p[0] = ('array', p[1], p[4])

def p_class_statement(p):
    '''class_statement : CLASS IDENTIFIER LBRACE class_body RBRACE'''
    p[0] = ('class', p[2], p[4])

def p_class_body(p):
    '''class_body : class_body_element
                  | class_body class_body_element'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_class_body_element(p):
    '''class_body_element : assignment_statement
                          | function_statement'''
    p[0] = p[1]

def p_function_statement(p):
    '''function_statement : FUNCTION IDENTIFIER LPAREN parameter_list RPAREN LBRACE statement_list RBRACE'''
    p[0] = ('function', p[2], p[4], p[7])

def p_parameter_list(p):
    '''parameter_list : VARIABLE
                      | parameter_list COMMA VARIABLE
                      | empty'''
    if len(p) == 2:
        p[0] = [p[1]] if p[1] else []
    else:
        p[0] = p[1] + [p[3]]

# Estructura de Datos: Declaracion de objetos
def p_object_declaration(p):
    '''object_declaration : VAR VARIABLE EQUALS NEW CLASS LPAREN RPAREN SEMI'''

# Estructura de Control: While
def p_while_statement(p):
    '''while_statement : WHILE LPAREN expression RPAREN statements'''

# Funcion: Funcion Variable
def p_function_variable(p):
    '''function_variable : FUNCTION VARIABLE LPAREN RPAREN LBRACE statements RBRACE'''

# Impresion
def p_print_statement(p):
    '''print_statement : ECHO LPAREN expression_list RPAREN SEMI
                       | ECHO expression_list SEMI'''

# Solicitud de Datos
def p_input_statement(p):
    '''input_statement : VARIABLE EQUALS READLINE LPAREN RPAREN SEMI'''

# Expresiones Aritmeticas
def p_expression_statement(p):
    '''expression_statement : expression SEMI'''

#Fin - Enrique Zambrano

# Inicio - Alejandro Barrera 



# Estructura de Datos: Declaración de arreglos
def p_array(p):
    '''array : ARRAY LPAREN arrayArg RPAREN SEMI'''
    
def p_arrayArg(p):
    '''arrayArg : index ARROW value
                | index ARROW value arrayArg
                | index ARROW value COMMA arrayArg'''
    
def p_index(p):
    '''index : INTEGER
            | STRING'''

# Estructura de Control: if y else
def p_ifStatement(p):
    '''ifStatement : IF LPAREN condition RPAREN LBRACE statements RBRACE SEMI
                    | IF LPAREN condition RPAREN LBRACE statements RBRACE elseStatement'''
    
def p_elseStatement(p):
    '''elseStatement : ELSE LBRACE statements RBRACE SEMI'''
    
def p_statements(p):
    '''statements : expression
                | impression
                | array
                | declaration'''
    
def p_declaration(p):
  '''declaration : VARIABLE EQUALS value
                | VARIABLE EQUALS array'''
    
def p_impression(p):
    'impression : ECHO LPAREN value RPAREN'
        
def p_condition(p):
    'condition : value compOperator value'
    
def p_expression(p):
    'expression : value operator value'
    
def p_expression_list(p):
    '''expression_list : expression
                        | expression COMMA expression'''
    
def p_compOperator(p):
    '''compOperator : LT
                    | GT
                    | LE
                    | GE
                    | EQ
                    | NE'''
    
def p_operator(p):
    '''operator : PLUS
                | MINUS
                | TIMES
                | DIVIDE'''
    
def p_value(p):
    '''value : VARIABLE
            | INTEGER
            | FLOAT
            | expression_statement'''
    
#Función: Funciones de flecha.
def p_arrowFunction(p):
    '''arrowFunction : FUNCTION LPAREN VARIABLE RPAREN ARROW expression SEMI
                    | FUNCTION LPAREN VARIABLE RPAREN ARROW arrowFunction'''

#Fin - Alejandro Barrera

#-----------TODO PRATT------------

def p_class_declaration(p):
    '''class_declaration : CLASS IDENTIFIER LBRACE class_body RBRACE'''

def p_class_body(p):
    '''class_body : class_member_list'''

def p_class_member_list(p):
    '''class_member_list : class_member_list class_member
                         | EMPTY'''

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
                      | EMPTY'''

def p_parameter(p):
    '''parameter : VARIABLE'''

def p_statement_list(p):
    '''statement_list : statement_list statements
                      | EMPTY'''

def p_condition(p):
    '''condition : expression comparison_operator expression
                 | condition logical_operator condition'''
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3])
    else:
        p[0] = (p[2], p[1], p[3])

def p_comparison_operator(p):
    '''comparison_operator : EQ
                           | NE
                           | LT
                           | LE
                           | GT
                           | GE'''
    p[0] = p[1]

def p_logical_operator(p):
    '''logical_operator : AND
                        | OR
                        | NOT'''
    p[0] = p[1]

def p_expression(p):
    '''expression : term
                  | expression PLUS term
                  | expression MINUS term
                  | expression TIMES term
                  | expression DIVIDE term
                  | expression MOD term
                  | expression EXP term'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])

def p_term(p):
    '''term : INTEGER
            | FLOAT
            | STRING
            | VARIABLE
            | LPAREN expression RPAREN'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

def p_empty(p):
    '''empty :'''
    p[0] = None

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}' (line {p.lineno})")
    else:
        print("Syntax error at EOF")

# Construir el parser
parser = yacc.yacc()

# Función para realizar pruebas y generar logs
def test_parser(data, username):
    result = parser.parse(data)
    log_folder = "logs"
    os.makedirs(log_folder, exist_ok=True)
    current_time = datetime.datetime.now().strftime("%d%m%Y-%Hh%M")
    filename = f"parser-{username}_{current_time}.txt"
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