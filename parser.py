import ply.yacc as yacc
from docutils.parsers import null

from lexer import tokens
import datetime
import os

variables ={}
constants={}
defined_exceptions = ['CustomException', 'AnotherException']
def p_statement(p):
    '''statement : print SEMI
                 | declaration SEMI
                 | input SEMI
                 | expression SEMI
                 | object_declaration
                 | class_declaration
                 | array_declaration SEMI
                 | property_declaration SEMI
                 | function_statement
                 | function_variable
                 | function_anonymous
                 | function_arrow
                 | class_statement
                 | while
                 | constant_declaration
                 | constant_use
                 | try_catch
                 | catch_item
                 | if'''
    
def p_statements(p):
    '''statements : statement statements
                | statement'''
    
def p_declaration(p):
    '''declaration : VARIABLE SET value
                    | VARIABLE SET STRING
                    | VARIABLE SET expression
                    | VARIABLE SET condition'''
    variables[p[1]] = p[3]        #Enrique Zambrano
    if isinstance(p[3], str) and p[3] not in variables:
        print(f"Error semántico: la variable '{p[3]}' no ha sido inicializada.")
    
def p_class_statement(p):          #Enrique Zambrano
    '''class_statement : CLASS IDENTIFIER LBRACE class_member_list RBRACE'''
    p[0] = ('class', p[2], p[4])
    validate_class_members(p[2], p[4])

def validate_class_members(class_name, member_list):        #Enrique Zambrano
    if not member_list:
        raise Exception(f"Error semántico: la clase {class_name} no tiene miembros.")
    for member in member_list:
        if member[0] not in ['property', 'method', 'constructor']:
            raise Exception(f"Error semántico: miembro {member[1]} en la clase {class_name} no es válido.")


def p_function_statement(p):
    '''function_statement : FUNCTION IDENTIFIER LPAREN parameters RPAREN LBRACE statements RBRACE'''
    p[0] = ('function', p[2], p[4], p[7])

# Estructura de Control: While
def p_while(p):
    '''while : WHILE LPAREN expression RPAREN LBRACE statements RBRACE'''


# Funcion: Funcion Variable
def p_function_variable(p):
    '''function_variable : FUNCTION VARIABLE LPAREN RPAREN LBRACE statements RBRACE'''


# Impresion
def p_print(p):
    '''print : ECHO LPAREN value RPAREN
            | ECHO value
            | ECHO STRING'''
        
    if (len(p) == 5):    
        if not isinstance(p[3], str) or p[3] in variables:
            pass
        else:
            print(f"Error semántico: la variable {p[3]} no ha sido inicializada.")
            return

# Solicitud de Datos
def p_input(p):
    'input : VARIABLE SET READLINE LPAREN RPAREN'
    
# Estructura de Datos: Declaracion de objetos
def p_object_declaration(p):
    'object_declaration : VAR VARIABLE SET NEW CLASS LPAREN RPAREN SEMI'

# Estructura de Datos: Declaración de arreglos
def p_array_declaration(p):
    '''array_declaration : VARIABLE SET ARRAY LPAREN arrayArg RPAREN
                        | VARIABLE SET ARRAY LPAREN empty RPAREN'''


def p_arrayArg(p):
    '''arrayArg : index ARROW value
                | index ARROW value arrayArg
                | index ARROW value COMMA arrayArg'''


# Estructura de Control: if y else
def p_if(p):
    '''if : IF LPAREN condition RPAREN LBRACE statements RBRACE SEMI
            | IF LPAREN conditions RPAREN LBRACE statements RBRACE SEMI
            | IF LPAREN condition RPAREN LBRACE statements RBRACE elseif
            | IF LPAREN condition RPAREN LBRACE statements RBRACE else'''
    
    if p[3] == null:
        print(f"Error semántico: Falta poner una condición.")
        return


def p_else(p):
    '''else : ELSE LBRACE statements RBRACE SEMI'''


def p_condition(p):
    'condition : value comparison_operator value'
    if not isinstance(p[1], str) or p[1] in variables:
        pass
    else:
        print(f"Error semántico: la variable {p[1]} no ha sido inicializada.")
        return
        
    if not isinstance(p[3], str) or p[3] in variables:
        pass
    else:
        print(f"Error semántico: la variable {p[3]} no ha sido inicializada.")
        return
        
def p_conditions(p):
    '''conditions : LBRACE condition RBRACE logical_operator conditions
                    | LBRACE condition RBRACE'''

def p_index(p):
    '''index : INTEGER
            | STRING'''


#Función: Funciones de flecha.
def p_function_arrow(p):
    '''function_arrow : FUNCTION LPAREN VARIABLE RPAREN ARROW expression SEMI
                    | FUNCTION LPAREN VARIABLE RPAREN ARROW function_arrow'''



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
    
    if isinstance(p[1], str) and p[1] in variables:
        p[0] = variables[p[1]];
    else:
        p[0] = p[1];


def p_operator(p):
    '''operator : PLUS
                | MINUS
                | TIMES
                | DIVIDE'''
    
def p_expression(p):
    'expression : value operator value'
    
    if not isinstance(p[1], str) or p[1] in variables:
        pass
    else:
        print(f"Error semántico: la variable {p[1]} no ha sido inicializada.")
        return
        
    if not isinstance(p[3], str) or p[3] in variables:
        pass
    else:
        print(f"Error semántico: la variable {p[3]} no ha sido inicializada.")
        return
        
    #Aporte Alejandro: Revisa que, de usarse una variable en la expresión. Esta haya sido inicializada.
    


def p_expressions(p):
    '''expressions : expression COMMA expressions
                    | expression'''

def p_class_declaration(p):
    '''class_declaration : CLASS IDENTIFIER LBRACE class_body RBRACE'''


def p_class_body(p):
    '''class_body : class_member_list'''


def p_class_member_list(p):
    '''class_member_list : class_member class_member_list
                         | class_member'''


def p_class_member(p):
    '''class_member : property_declaration
                    | method_declaration
                    | constructor_declaration'''


#Inicio Regla semantica Pratt Garcia
def p_constant_declaration(p):
    '''constant_declaration : DEFINE LPAREN STRING COMMA expression RPAREN SEMI
                            | CONST IDENTIFIER SET expression SEMI'''
    if p[1] == 'define':
        constant_name = p[3]
        constant_value = p[5]
        if constant_name in constants:
            print(f"Error: Constant '{constant_name}' is already defined.")
        else:
            constants[constant_name] = constant_value
    else:
        constant_name = p[2]
        constant_value = p[4]
        if constant_name in constants:
            print(f"Error: Constant '{constant_name}' is already defined.")
        else:
            constants[constant_name] = constant_value

def p_constant_use(p):
    '''constant_use : IDENTIFIER'''
    constant_name = p[1]
    if constant_name not in constants:
        print(f"Error: Constant '{constant_name}' is not defined.")

def p_try_catch(p):
    '''try_catch : TRY LBRACE statements RBRACE catch_list'''
    p[0] = ('try_catch', p[3], p[5])

def p_catch_list(p):
    '''catch_list : catch_item catch_list
                  | empty'''
    if len(p) == 3:
        p[0] = [p[1]] + (p[2] if p[2] else [])
    else:
        p[0] = []

def p_catch_item(p):
    '''catch_item : CATCH LPAREN EXCEPTION VARIABLE RPAREN LBRACE statements RBRACE'''
    # Añadir manejo semántico aquí, por ejemplo:
    exception_type = p[3]
    exception_variable = p[4]
    # Verificar si la excepción es genérica o específica
    if exception_type != 'Exception':
        # Validar que la excepción esté definida o sea manejada adecuadamente
        if exception_type not in defined_exceptions:
            print(f"Error semántico: Excepción '{exception_type}' no definida.")
        # Asegurarse de que la variable de excepción se maneje correctamente
        if exception_variable not in variables:
            print(f"Error semántico: Variable '{exception_variable}' no definida para capturar la excepción.")
    else:
        # Excepción genérica, no se requiere una variable
        if exception_variable is not None:
            print(f"Error semántico: No se espera variable para la excepción genérica '{exception_type}'.")

    p[0] = ('catch_item', exception_type, exception_variable, p[7])

#Fin Pratt Garcia

def p_property_declaration(p):
    '''property_declaration : visibility VARIABLE'''


def p_method_declaration(p):
    '''method_declaration : visibility FUNCTION IDENTIFIER LPAREN parameters RPAREN LBRACE statements RBRACE'''


def p_constructor_declaration(p):
    '''constructor_declaration : visibility FUNCTION CONSTRUCT LPAREN parameters RPAREN LBRACE statements RBRACE'''


def p_visibility(p):
    '''visibility : PUBLIC
                  | PROTECTED
                  | PRIVATE'''


def p_parameters(p):
    '''parameters : parameter COMMA parameters
                    | parameter'''


def p_parameter(p):
    '''parameter : TYPE VARIABLE
                 | VARIABLE'''


# Definicion del elseif
def p_elseif(p):
    '''elseif : ELSEIF LPAREN condition RPAREN LBRACE statements RBRACE
                | ELSEIF LPAREN condition RPAREN LBRACE statements RBRACE else'''


# Funciones anonimas
def p_function_anonymous(p):
    '''function_anonymous : FUNCTION LPAREN parameters RPAREN use_clause_opt LBRACE statements RBRACE'''


def p_use_clause_opt(p):
    'use_clause_opt : USE LPAREN variables RPAREN'


def p_variables(p):
    '''variables : VARIABLE COMMA variables
                | VARIABLE'''


def p_logical_operator(p):
    '''logical_operator : AND
                        | OR'''

def p_empty(p):
    '''empty :'''
    pass

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
            if s == "close":
                break
            result = parser.parse(s)
            print(result)
            log_file.write(str(result))



test_parser("A1ej00")
