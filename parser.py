import ply.yacc as yacc
from lexer import tokens
import datetime
import os

# Inicio - Enrique Zambrano 

# Estructura de Datos: Declaracion de objetos
def p_object_declaration(p):
    '''object_declaration : VAR VARIABLE EQUALS NEW CLASS LPAREN RPAREN SEMI'''

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
    '''input_statement : VARIABLE EQUALS READLINE LPAREN RPAREN SEMI'''

# Expresiones Aritmeticas
def p_expression_statement(p):
    '''expression_statement : expression SEMI'''

#Fin - Enrique Zambrano

#-----------TODO PRATT & ALEJANDRO------------

parser = yacc.yacc()


def test_parser(data, username):
    result = parser.parse(data)
    log_folder = "logs"
    os.makedirs(log_folder, exist_ok=True)
    current_time = datetime.datetime.now().strftime("%d%m%Y-%Hh%M")
    log_filename = f"sintactico-{username}-{current_time}.txt"
    log_path = os.path.join(log_folder, log_filename)

    with open(log_path, "w") as log_file:
        if result:
            log_file.write(str(result))
            print(result)
        else:
            log_file.write("Syntax errors found")
            print("Syntax errors found")


