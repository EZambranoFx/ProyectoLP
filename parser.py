import ply.yacc as yacc
from lexer import tokens
import datetime
import os

date = datetime.datetime.now().strftime("%d%m%Y-%Hh%M")
username = input('set username: ')
log_folder = "logs"
os.makedirs(log_folder, exist_ok=True)
filename = f"Sintactico-{username}-{date}.txt"


variables ={}
constants={}
defined_exceptions = ['CustomException', 'AnotherException']
def p_statement(p):
    '''statement : print SEMI
                 | print_error
                 | declaration SEMI
                 | declaration_error
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
                 | while
                 | constant_declaration
                 | constant_use
                 | try_catch
                 | catch_item
                 | throw_statement
                 | if'''
    
    
def p_statements(p):
    '''statements : statement statements
                | statement'''
    
def p_declaration(p):
    '''declaration : VARIABLE SET value
                    | VARIABLE SET STRING
                    | VARIABLE SET expression
                    | VARIABLE SET condition'''
    
    variables[p[1]] = p[3]
    
def p_declaration_error(p):
    'declaration_error : VARIABLE SET error'
    print("Syntax error in declaration statement. Bad expression")
    log_file.write("Syntax error in declaration statement. Bad expression")
    log_file.write("\n")
    
def p_function_statement(p):
    '''function_statement : visibility FUNCTION IDENTIFIER LPAREN parameters RPAREN LBRACE statements RBRACE'''

# Estructura de Control: While
def p_while(p):
    '''while : WHILE LPAREN condition RPAREN LBRACE statements RBRACE'''


# Funcion: Funcion Variable
def p_function_variable(p):
    '''function_variable : FUNCTION VARIABLE LPAREN RPAREN LBRACE statements RBRACE'''



# Impresion
def p_print(p):
    '''print : ECHO LPAREN value RPAREN
            | ECHO value
            | ECHO LPAREN STRING RPAREN
            | ECHO STRING'''
        
    if (len(p) == 5):    
        if not isinstance(p[3], str) or p[3] in variables:
            pass
        else:
            print(f"Error semántico: la variable {p[3]} no ha sido inicializada.")
            return
        
def p_print_error(p):
    'print_error : ECHO error'
    print("Syntax error in print statement. Bad expression")
    log_file.write("Syntax error in print statement. Bad expression")
    log_file.write("\n")
    
    

# Solicitud de Datos
def p_input(p):
    'input : VARIABLE SET READLINE LPAREN STRING RPAREN'
    
# Estructura de Datos: Declaracion de objetos
def p_object_declaration(p):
    'object_declaration : VAR VARIABLE SET NEW CLASS LPAREN RPAREN SEMI'

# Estructura de Datos: Declaración de arreglos
def p_array_declaration(p):
    '''array_declaration : VARIABLE SET ARRAY LPAREN arrayArg RPAREN
                        | VARIABLE SET ARRAY LPAREN empty RPAREN'''


def p_arrayArg(p):
    '''arrayArg : index ARROW value
                | index ARROW value COMMA arrayArg'''


# Estructura de Control: if y else
def p_if(p):
    '''if : IF LPAREN conditions RPAREN LBRACE statements RBRACE
            | IF LPAREN conditions RPAREN LBRACE statements RBRACE elseif
            | IF LPAREN conditions RPAREN LBRACE statements RBRACE else'''

# Definicion del elseif
def p_elseif(p):
    '''elseif : ELSEIF LPAREN conditions RPAREN LBRACE statements RBRACE
                | ELSEIF LPAREN conditions RPAREN LBRACE statements RBRACE elseif
                | ELSEIF LPAREN conditions RPAREN LBRACE statements RBRACE else'''

def p_else(p):
    '''else : ELSE LBRACE statements RBRACE'''


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
    '''conditions : condition logical_operator conditions
                    | condition '''

def p_index(p):
    '''index : INTEGER
            | STRING'''


#Función: Funciones de flecha.
def p_function_arrow(p):
    '''function_arrow : VARIABLE SET FUNCTION LPAREN VARIABLE RPAREN ARROW expression SEMI
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
            | constant_use
            | FLOAT'''
    
    if isinstance(p[1], str) and p[1] in variables:
        p[0] = variables[p[1]];
    else:
        p[0] = p[1];

    if isinstance(p[1], str) and p[1] in constants:
        print(p[1])
        p[0] = constants[p[1]]
    else:
        p[0] = p[1]


def p_operator(p):
    '''operator : PLUS
                | MINUS
                | TIMES
                | DIVIDE'''
    
def p_expression(p):
    '''expression : value operator value
                  | value'''
    
    if not isinstance(p[1], str) or p[1] in variables:
        pass
    else:
        print(f"Error semántico: la variable {p[1]} no ha sido inicializada.")
        return

    if len(p) == 4:  # Si la producción tiene tres partes: value operator value
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

        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
        elif p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]
    else:
        p[0] = p[1]

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
            print(f"Error semantico: La constante '{constant_name}' ya esta definida.")
        else:
            constants[constant_name] = constant_value
    else:
        constant_name = p[2]
        constant_value = p[4]
        if constant_name in constants:
            print(f"Error semantico: La constante '{constant_name}' ya esta definida.")
        else:
            constants[constant_name] = constant_value
    print(constants)

def p_constant_use(p):
    '''constant_use : IDENTIFIER'''
    constant_name = p[1]
    if constant_name not in constants:
        print(f"Error semantico: La constante '{constant_name}'no esta definida.")
        p[0] = 0
    else:
        p[0] = constants[constant_name]

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
    '''catch_item : CATCH LPAREN EXCEPTION VARIABLE RPAREN LBRACE statements RBRACE
                  | CATCH LPAREN EXCEPTION empty RPAREN LBRACE statements RBRACE'''
    exception_type = p[3]
    exception_variable = p[4]
    # Verificar si la excepción es genérica o específica
    if exception_type != 'Exception':
        # Validar que la excepción esté definida o sea manejada adecuadamente
        if exception_type not in defined_exceptions:
            print(f"Error semántico: Excepción '{exception_type}' no definida.")
        # Asegurarse de que la variable de excepción se maneje correctamente
        if exception_variable not in variables:
            print(variables)
            print(f"Error semántico: Variable '{exception_variable}' no definida para capturar la excepción.")
    else:
        if exception_variable is not None:
            print(f"Error semántico: No se espera variable para la excepción genérica '{exception_type}'.")

    p[0] = ('catch_item', exception_type, exception_variable, p[7])


def p_throw_statement(p):
    '''throw_statement : THROW NEW EXCEPTION LPAREN RPAREN SEMI'''
    p[0] = ('throw', p[3])

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
                    | parameter
                    | IDENTIFIER
                    | empty'''


def p_parameter(p):
    '''parameter : TYPE VARIABLE
                 | VARIABLE'''


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
    p[0] = None
    pass

# Error rule for syntax errors
def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}', line {p.lineno}")
    else:
        print("Syntax error at EOF")


parser = yacc.yacc()

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
        log_file.write('calc > ' + s)
        log_file.write("\n\n")

