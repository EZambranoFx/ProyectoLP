import ply.yacc as yacc
from lexer import tokens
import datetime
import os

variables ={}
# Inicio - Enrique Zambrano

def p_statement(p):
    '''statement : print SEMI
                 | input SEMI
                 | expression SEMI
                 | declaration SEMI
                 | object_declaration
                 | class_declaration
                 | array_declaration
                 | data_structure
                 | function_statement
                 | function_variable
                 | function_anonymous
                 | class_statement
                 | while
                 | array'''
    
def p_statements(p):
    '''statements : statement statements
                | statement'''
    
def p_declaration(p):
    '''declaration : VARIABLE SET expression
                    | VARIABLE SET condition'''
    variables[p[1]]=p[3]        #Enrique Zambrano
    
def p_data_structure(p):
    '''data_structure : array
                    | class_statement'''
    
def p_class_statement(p):
    '''class_statement : CLASS IDENTIFIER LBRACE class_body RBRACE'''
    p[0] = ('class', p[2], p[4])

def p_function_statement(p):
    '''function_statement : FUNCTION IDENTIFIER LPAREN parameter_list RPAREN LBRACE statements RBRACE'''
    p[0] = ('function', p[2], p[4], p[7])

# Estructura de Control: While
def p_while(p):
    '''while : WHILE LPAREN expression RPAREN LBRACE statements RBRACE'''


# Funcion: Funcion Variable
def p_function_variable(p):
    '''function_variable : FUNCTION VARIABLE LPAREN RPAREN LBRACE statements RBRACE'''


# Impresion
def p_print(p):
    '''print : ECHO LPAREN expressions RPAREN
                       | ECHO expressions'''


# Solicitud de Datos
def p_input(p):
    '''input : VARIABLE SET READLINE LPAREN RPAREN
            | empty'''
    
# Estructura de Datos: Declaracion de objetos
def p_object_declaration(p):
    'object_declaration : VAR VARIABLE SET NEW CLASS LPAREN RPAREN SEMI'

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
def p_if(p):
    '''if : IF LPAREN condition RPAREN LBRACE statements RBRACE SEMI
                    | IF LPAREN condition RPAREN LBRACE statements RBRACE elseif
                    | IF LPAREN condition RPAREN LBRACE statements RBRACE else'''


def p_else(p):
    '''else : ELSE LBRACE statements RBRACE SEMI'''


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
            | FLOAT'''



# Fin - Alejandro Barrera

# Inicio - Pratt Garcia

def p_operator(p):
    '''operator : PLUS
                | MINUS
                | TIMES
                | DIVIDE'''
    
def p_expression(p):
    'expression : value operator value'


def p_expressions(p):
    '''expressions : expression COMMA expressions
                       | expression'''


def p_empty(p):
    '''empty :'''
    pass

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
    '''method_declaration : visibility FUNCTION IDENTIFIER LPAREN parameter_list RPAREN LBRACE statements RBRACE'''


def p_constructor_declaration(p):
    '''constructor_declaration : visibility FUNCTION CONSTRUCT LPAREN parameter_list RPAREN LBRACE statements RBRACE'''


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


# Definicion del elseif
def p_elseif(p):
    '''elseif : ELSEIF LPAREN condition RPAREN LBRACE statements RBRACE
                | ELSEIF LPAREN condition RPAREN LBRACE statements RBRACE else'''


# Funciones anonimas
def p_function_anonymous(p):
    '''function_anonymous : FUNCTION LPAREN parameter_list RPAREN use_clause_opt LBRACE statements RBRACE'''


def p_use_clause_opt(p):
    '''use_clause_opt : USE LPAREN variable_list RPAREN
                      | empty'''


def p_variable_list(p):
    '''variable_list : variable_list COMMA VARIABLE
                     | VARIABLE'''


def p_logical_operator(p):
    '''logical_operator : AND
                        | OR'''


# Declarar Estructuras de Datos
def p_array_declaration(p):
    '''array_declaration : VARIABLE SET ARRAY LPAREN array_elements RPAREN SEMI'''


def p_array_elements(p):
    '''array_elements : array_elements COMMA array_element
                      | array_element
                      | empty'''


def p_array_element(p):
    '''array_element : expression
                     | expression ARROW expression'''

# Fin - Pratt Garcia

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()


def test_parser(username):
    log_folder = "logs"
    os.makedirs(log_folder, exist_ok=True)
    current_time = datetime.datetime.now().strftime("%d%m%Y-%Hh%M")
    filename = f"Sintactico-{username}-{current_time}.txt"
    
    with open(os.path.join(log_folder, filename), 'w') as log_file:
        while True:
            try:
                s = input('calc > ')
            except EOFError:
                break
            if not s: continue
            result = parser.parse(s)
            print(result)
            log_file.write(str(result))

#Inicio - Enrique Zambrano
AlgoritmoEnriqueZambrano = '''
<?php
// Ejemplo de código PHP
function suma($a, $b) {
    return $a + $b;
}

// Llamada a la función
$resultado = suma(5, 3);
echo "El resultado de la suma es: " . $resultado;
?>

'''
#test_parser(AlgoritmoEnriqueZambrano, "EnriqueZambrano")
#Fin - Enrique Zambrano

test_parser("A1ej00")
