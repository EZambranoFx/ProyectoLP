import ply.lex as lex
import datetime
import os

#Poner aqui los tokens
# Definición de los tokens
tokens=[
#TODO
]
# Definición de las palabras reservadas
reserved = {
    #inicio - Enrique Zambrano
    'if': 'IF', 
    'else': 'ELSE', 
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
    'throw': 'THROW'
    #Fin - Enrique Zambrano
}
tokens += list(reserved.values())
# Definición de los patrones de los tokens

#----------TODO pratt & Alejandro---------

#Inicio - Enrique Zambrano
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_COMMENT(t):
    r'//.*|/\*[^*]*\*+(?:[^/*][^*]*\*+)*/|#.*'
    pass  # Ignorar comentarios

t_STRING  = r'\"([^\\\n]|(\\.))*?\"'
#Fin - Enrique Zambrano

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

