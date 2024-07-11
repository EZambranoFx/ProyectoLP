import tkinter as tk
from tkinter import messagebox
import ply.lex as lex
import ply.yacc as yacc
import datetime
import os

# Lexer code (lexer.py)
# Definición de los tokens y reglas del lexer
tokens = [
    # inicio - Alejandro Barrera
    'PHP_OPEN',
    'PHP_CLOSE',
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
    'DOLLAR',
    'USE',
    'TYPE',
    # fin - Alejandro Barrera
    # inicio - Pratt Garcia
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
    'ERROR'

    # fin - Pratt Garcia
]

# Definición de las palabras reservadas
reserved = {
    # inicio - Enrique Zambrano
    'if': 'IF',
    'else': 'ELSE',
    'elseif':'ELSEIF',
    'array' : 'ARRAY',
    'while': 'WHILE',
    'for': 'FOR',
    'return': 'RETURN',
    'function': 'FUNCTION',
    'class': 'CLASS',
    'public': 'PUBLIC',
    'protected': 'PROTECTED',
    'private': 'PRIVATE',
    'static': 'STATIC',
    'const': 'CONST',
    'define': 'DEFINE',
    'var': 'VAR',
    'new': 'NEW',
    'echo': 'ECHO',
    'Exception': 'EXCEPTION',
    'construct': 'CONSTRUCT',
    'throw': 'THROW',
    'try': 'TRY',
    'catch': 'CATCH',
    'CustomException': 'EXCEPTION',
    'AnotherException': 'EXCEPTION',
    'readline': 'READLINE'
    # fin - Enrique Zambrano
}

tokens += list(reserved.values())

# Inicio - Alejandro Barrera
t_SET     = r'\='
t_DOLLAR  = r'\$'
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_MOD     = r'%'
t_ARROW   = r'=>'
t_COMMA   = r','

# Inicio - Pratt Garcia
t_PHP_OPEN = r'<\?php'
t_PHP_CLOSE = r'\?>'
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
t_USE = r'use'
t_TYPE = r'\b(int|float|string|bool|array|object|void)\b'
t_DEFINE = r'define'
t_THROW = r'throw'
t_TRY = r'try'
t_CATCH = r'catch'
t_EXCEPTION = r'Exception'

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

def t_READLINE(t):
    r'readline\s*\(\s*\)'
    return t


#Fin - Pratt Garcia

# Definición de los patrones de los tokens



def t_FUNCTION(t):
    r'function'
    t.value = 'function'
    return t

def t_VARIABLE(t):
    r'\$[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t
# fin - Alejandro Barrera

# Inicio - Enrique Zabrano
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_COMMENT(t):
    r'//.*|/\*[^*]*\*+(?:[^/*][^*]*\*+)*/|\#.*'
    pass  # Ignorar comentarios

def t_STRING(t):
    r'(\"([^\\\n]|(\\.))*?\"|\'([^\\\n]|(\\.))*?\')'
    if t.value.startswith('"'):
        t.value = t.value.strip('"')
    elif t.value.startswith("'"):
        t.value = t.value.strip("'")
    t.type = 'STRING'
    return t
# fin - Enrique Zambrano

# Ignorar espacios en blanco y tabuladores
t_ignore = ' \t'

# Regla para manejar errores
def t_error(t):
    #print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Parser code (parser.py)
# Definición del parser y reglas del parser
variables = {}
constants = {}
defined_exceptions = ['CustomException', 'AnotherException']


def p_statement(p):
    '''statement : print SEMI
                 | print_error
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
                 | while
                 | constant_declaration
                 | constant_use
                 | try_catch
                 | catch_item
                 | if
                 | empty'''


def p_statements(p):
    '''statements : statement statements
                | statement'''


def p_declaration(p):
    '''declaration : VARIABLE SET value
                    | VARIABLE SET STRING
                    | VARIABLE SET expression
                    | VARIABLE SET condition'''

    variables[p[1]] = p[3]


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


# Función: Funciones de flecha.
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

    # Aporte Alejandro: Revisa que, de usarse una variable en la expresión. Esta haya sido inicializada.


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


# Inicio Regla semantica Pratt Garcia
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
    print(constants)


def p_constant_use(p):
    '''constant_use : IDENTIFIER'''
    constant_name = p[1]
    if constant_name not in constants:
        print(f"Error: Constant '{constant_name}' is not defined.")
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


# Fin Pratt Garcia

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


# Definicion del elseif
def p_elseif(p):
    '''elseif : ELSEIF LPAREN condition RPAREN LBRACE statements RBRACE elseif
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
    p[0] = None
    pass


# Error rule for syntax errors
def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}', line {p.lineno}")
    else:
        print("Syntax error at EOF")

# Inicialización del lexer y parser
lexer = lex.lex()
parser = yacc.yacc()

# Función para realizar pruebas y generar logs
def test_lexer(data, username):
    lexer.input(data)
    log_folder = "logs"
    os.makedirs(log_folder, exist_ok=True)
    current_time = datetime.datetime.now().strftime("%d%m%Y-%Hh%M")
    log_filename = f"lexico-{username}-{current_time}.txt"
    log_path = os.path.join(log_folder, log_filename)

    with open(log_path, "w", encoding="utf-8") as log_file:
        while True:
            tok = lexer.token()
            if not tok:
                break
            log_file.write(f"{tok.type}: {tok.value} (line {tok.lineno})\n")
            print(f"{tok.type}: {tok.value} (line {tok.lineno})")

# Función para comprobar el texto introducido
def check_code():
    code = test_string_entry.get("1.0", tk.END).strip()
    if not code:
        messagebox.showwarning("Empty Input", "Please enter code to check.")
        return

    # Log folder setup
    log_folder = "logs"
    os.makedirs(log_folder, exist_ok=True)
    current_time = datetime.datetime.now().strftime("%d%m%Y-%Hh%M")
    log_filename = f"Sintactico-{current_time}.txt"
    log_path = os.path.join(log_folder, log_filename)

    with open(log_path, 'w') as log_file:
        try:
            result = parser.parse(code)
            output_label.config(text="OK", bg="green")
            log_file.write(f"Result: {result}\n")
        except Exception as e:
            output_label.config(text=f"ERROR: {e}", bg="red")
            log_file.write(f"ERROR: {e}\n")

def clear_entries():
    regex_entry.delete(0, tk.END)
    test_string_entry.delete("1.0", tk.END)
    output_label.config(text="SALIDA OK/ERROR", bg="grey")

# Create the main window
root = tk.Tk()
root.title("Code Checker")
root.configure(bg="black")

# Create and place the widgets
tk.Label(root, text="Expresión Regular", bg="black", fg="white").grid(row=0, column=0, padx=10, pady=10, sticky="w")
regex_entry = tk.Entry(root, width=50)
regex_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Texto de prueba", bg="black", fg="white").grid(row=1, column=0, padx=10, pady=10, sticky="nw")
test_string_entry = tk.Text(root, width=50, height=10)
test_string_entry.grid(row=1, column=1, padx=10, pady=10)

check_button = tk.Button(root, text="COMPROBAR", command=check_code, bg="green", fg="white", width=20)
check_button.grid(row=2, column=1, padx=10, pady=10, sticky="w")

clear_button = tk.Button(root, text="LIMPIAR", command=clear_entries, bg="red", fg="white", width=20)
clear_button.grid(row=2, column=1, padx=10, pady=10, sticky="e")

output_label = tk.Label(root, text="SALIDA OK/ERROR", bg="grey", fg="white", width=50, height=2)
output_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()
