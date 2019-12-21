import ply.lex as lex


reserved = {
    # type
    'int': 'INT',
    'double': 'DOUBLE',
    'float': 'FLOAT',
    'char': 'CHAR',
    'void': 'VOID',
    'bool': 'BOOL',
    'auto': 'AUTO',
    'array': 'ARRAY',

    # control
    'return': 'RETURN',
    'break': 'BREAK',
    'continue': 'CONTINUE',

    # branch
    'for': 'FOR',
    'while': 'WHILE',
    'do': 'DO',
    'if': 'IF',
    'else': 'ELSE',
    'switch': 'SWITCH',
    'case': 'CASE',
    'default': 'DEFAULT',

    # literal
    'true': 'TRUE',
    'false': 'FALSE',
}

tokens = [
    'PLUS',
    'MINUS',
    'MULTI',
    'DIVIDE',
    'PLUSEQU',
    'MINUSEQU',
    'MULTIEQU',
    'DIVIDEQU',
    
    'EQUAL',

    'CEQ',          # conditional equal
    'CNEQ',
    'CGT',
    'CLT',
    'CGE',
    'CLE',

    'AND',
    'OR',
    'NOT',

    'INV',          # bit operate
    'BAND',
    'BOR',
    'BANDEQU',
    'BOREQU',

    'PLUSELF',
    'MINUSELF',

    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'LSQUARE',
    'RSQUARE',

    'COMMA',
    'COLON',
    'SEMICOLON',

    'IDENTIFIER',
    'NUMBER',
    'DECIMAL',
    'CHARACTER',
    'STRING',
    
    'COMMETLINE',
    'COMMETBLOCK',
    'INCLUDE',
    
    'GOTO',
] + list(reserved.values())

t_COMMA = r','
t_COLON = r':'
t_SEMICOLON = r';'

t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTI = r'\*'
t_DIVIDE = r'/'
t_PLUSEQU = r'\+='
t_MINUSEQU = r'-='
t_MULTIEQU = r'\*='
t_DIVIDEQU = r'/='

t_EQUAL = r'='

t_CEQ = r'=='
t_CNEQ = r'!='
t_CGT = r'>'
t_CLT = r'<'
t_CGE = r'>='
t_CLE = r'<='

t_PLUSELF = r'\+\+'
t_MINUSELF = r'--'

t_NOT = r'!'
t_AND = r'&&'
t_OR = r'\|\|'

t_INV = r'~'
t_BAND = r'&'
t_BOR = r'\|'
t_BANDEQU = r'&='
t_BOREQU = r'\|='

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_LSQUARE = r'\['
t_RSQUARE = r'\]'


t_GOTO = r'=>'



# regular expression rules, with some actions


def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]* '
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_DECIMAL(t):
    r'((\d+\.\d+ | \.\d+ | \d+\.)) | ((\d+ | \d+\.\d+ | \.\d+ | \d+\.))(e|E)-?\d+'
    t.value = float(t.value)
    return t

def t_NUMBER(t):
    r'((0(x|X)[0-9A-Fa-f]+) | (0[0-7]*) | ([1-9]\d*))'
    if t.value.startswith('0x') or t.value.startswith('0X'):
        t.value = int(t.value, 16)
    elif t.value.startswith('0') and len(t.value) > 1:
        t.value = int(t.value, 8)
    else:
        t.value = int(t.value)
    return t

def t_CHARACTER(t):
    r'''
    \'( ([\w\W]) | (\\a) | (\\b) | (\\f) | (\\n) | (\\r) | (\\t) |
    (\\v) | (\\\\) | (\\\') | (\\\") | (\\\?) | (\\0) | (\\ooo) | (\\xhh) )\'
    '''
    t.value = t.value
    return t

def t_STRING(t):
    r'(\")([^\'\"]|\\\'|\\\")*(\")'
    t.value = t.value
    return t

# lexer to be ignored

def t_COMMETLINE(t):
    r'\/\/[^\n]*'

# record the line number skiped
def t_COMMETBLOCK(t):
    r'\/\*([^\*^\/]*|[\*^\/*]*|[^\**\/]*)*\*\/'
    t.lexer.lineno += t.value.count('\n')

def t_INCLUDE(t):
    r'\#include\s(\"[^\"]+\"| <[^<^>]+> )'
    t.lexer.lineno += 1

# record line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
