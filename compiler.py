import ply.lex as lex
import ply.yacc as yacc

# -----------------------
#   LEXICAL ANALYSIS
# -----------------------

tokens = (
    'NUMBER', 'ID',
    'SET', 'AS', 'DISPLAY',
    'IF', 'ELSE', 'WHILE',
    'LT', 'GT', 'EQEQ', 'NEQ',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'SEMI', 'EQUALS',
    'LBRACE', 'RBRACE'
)

# Operators & Symbols
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_SEMI    = r';'
t_EQUALS  = r'='
t_LT      = r'<'
t_GT      = r'>'
t_EQEQ    = r'=='
t_NEQ     = r'!='
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'

# Ignore spaces/tabs
t_ignore = ' \t'

# Keywords
def t_SET(t): r'set'; return t
def t_AS(t): r'as'; return t
def t_DISPLAY(t): r'display'; return t
def t_IF(t): r'if'; return t
def t_ELSE(t): r'else'; return t
def t_WHILE(t): r'while'; return t

# Identifiers & Numbers
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Newlines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling
def t_error(t):
    raise Exception(f"Illegal character '{t.value[0]}' at position {t.lexpos}")

lexer = lex.lex()

# -----------------------
#   SYNTAX PARSING
# -----------------------

variables = {}
output = ""

def p_program(p):
    'program : statement_list'
    global output
    output = "\n".join(p[1])

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + ([p[2]] if isinstance(p[2], str) else p[2])
    else:
        p[0] = [p[1]] if isinstance(p[1], str) else p[1]

def p_statement_set(p):
    'statement : SET ID AS expression SEMI'
    variables[p[2]] = p[4]
    p[0] = f"{p[2]} set to {p[4]}"

def p_statement_display(p):
    'statement : DISPLAY expression SEMI'
    p[0] = str(p[2])

def p_statement_if_else(p):
    'statement : IF expression LBRACE statement_list RBRACE ELSE LBRACE statement_list RBRACE'
    if p[2]:
        p[0] = p[4]
    else:
        p[0] = p[8]

def p_statement_while(p):
    'statement : WHILE expression LBRACE statement_list RBRACE'
    result = []
    condition = p[2]
    while eval_condition(condition):
        for stmt in p[4]:
            parser.parse(stmt + ';')
            result.append(stmt)
        # Re-evaluate the condition by reparsing the expression
        condition = parser.parse(p[2])
    p[0] = result

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression LT expression
                  | expression GT expression
                  | expression EQEQ expression
                  | expression NEQ expression'''
    if p[2] == '+': p[0] = p[1] + p[3]
    elif p[2] == '-': p[0] = p[1] - p[3]
    elif p[2] == '*': p[0] = p[1] * p[3]
    elif p[2] == '/':
        if p[3] == 0:
            raise Exception("Division by zero")
        p[0] = p[1] / p[3]
    elif p[2] == '<': p[0] = p[1] < p[3]
    elif p[2] == '>': p[0] = p[1] > p[3]
    elif p[2] == '==': p[0] = p[1] == p[3]
    elif p[2] == '!=': p[0] = p[1] != p[3]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_id(p):
    'expression : ID'
    if p[1] in variables:
        p[0] = variables[p[1]]
    else:
        raise Exception(f"Undefined variable '{p[1]}'")

def p_error(p):
    raise Exception("Syntax error")

parser = yacc.yacc()

# -----------------------
#   HELPER + RUN FUNCTION
# -----------------------

def eval_condition(cond):
    """Evaluate condition safely (used in loops)"""
    if isinstance(cond, bool): return cond
    if isinstance(cond, (int, float)): return cond != 0
    raise Exception("Invalid loop condition")

def run(code):
    global variables, output
    variables = {}
    output = ""
    try:
        parser.parse(code)
        return output
    except Exception as e:
        return f"[Compiler Error] {e}"
