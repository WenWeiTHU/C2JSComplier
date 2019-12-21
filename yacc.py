import ply.yacc as yacc
from lex import tokens


class Node:
    def __init__(self, type, children=None):
         self.type = type
         if children:
              self.children = children
         else:
              self.children = []


def pchildren(p):
    return list(p)[1:]


# start rule
def p_program(p):
    '''
    program : functions
            | e
    '''
    p[0] = Node('program', pchildren(p))

def p_e(p):
    '''
    e :
    '''
    p[0] = Node('empty')

def p_functions(p):
    '''
    functions : function
              | function functions
    '''
    p[0] = Node('functions', pchildren(p))

def p_function(p):
    '''
    function : func_ret IDENTIFIER LPAREN params RPAREN block
             | func_ret IDENTIFIER LPAREN RPAREN block
    '''
    p[0] = Node('function', pchildren(p))

def p_func_ret(p):
    '''
    func_ret : VOID
             | ARRAY
             | var_type
    '''
    p[0] = Node('function return', pchildren(p))

def p_var_type(p):
    '''
    var_type : INT
             | DOUBLE
             | FLOAT
             | CHAR
             | BOOL
    '''
    p[0] = Node('value type', pchildren(p))

def p_params(p):
    '''
    params : param
           | param COMMA params
    '''
    p[0] = Node('params', pchildren(p))

def p_param(p):
    '''
    param : var_type IDENTIFIER
          | var_type IDENTIFIER LSQUARE RSQUARE
          | ARRAY IDENTIFIER
    '''
    p[0] = Node('param', pchildren(p))

def p_block(p):
    '''
    block : LBRACE e RBRACE
          | LBRACE statements RBRACE
    '''
    p[0] = Node('block', pchildren(p))

def p_statements(p):
    '''
    statements : statement
               | statement statements
    '''
    p[0] = Node('statements', pchildren(p))

def p_statement(p):
    '''
    statement : declaration SEMICOLON
              | expression SEMICOLON
              | return SEMICOLON
              | BREAK SEMICOLON
              | CONTINUE SEMICOLON
              | for_block
              | while_block
              | do_while_block
              | if_block
              | switch_block
              | for_in_block
              | for_of_block
    '''
    p[0] = Node('statement', pchildren(p))

def p_switch_block(p):
    '''
    switch_block : SWITCH LPAREN expression RPAREN LBRACE case_blocks RBRACE
    '''
    p[0] = Node('switch_block', pchildren(p))

def p_case_blocks(p):
    '''
    case_blocks : e
                | default_block
                | case_block case_blocks
    '''
    p[0] = Node('case_blocks', pchildren(p))

def p_case_block(p):
    '''
    case_block : CASE expression COLON block
    '''
    p[0] = Node('case_block', pchildren(p))

def p_default_block(p):
    '''
    default_block : DEFAULT COLON block
    '''
    p[0] = Node('default_block', pchildren(p))

def p_if_block(p):
    '''
    if_block : IF LPAREN expression RPAREN block elif_blocks
    '''
    p[0] = Node('if_block', pchildren(p))

def p_elif_blocks(p):
    '''
    elif_blocks : e
                | else_block
                | elif_block elif_blocks
    '''
    p[0] = Node('elif_blocks', pchildren(p))

def p_elif_block(p):
    '''
    elif_block : ELSE IF LPAREN expression RPAREN block
    '''
    p[0] = Node('elif_block', pchildren(p))

def p_else_block(p):
    '''
    else_block : ELSE block
    '''
    p[0] = Node('else_block', pchildren(p))

def p_for_block(p):
    '''
    for_block : FOR LPAREN for_init SEMICOLON for_cond SEMICOLON for_update RPAREN block
    '''
    p[0] = Node('for_block', pchildren(p))

def p_for_init(p):
    '''
    for_init : e
             | declaration
             | expression
    '''
    p[0] = Node('for_init', pchildren(p))

def p_for_cond(p):
    '''
    for_cond : e
             | expression
    '''
    p[0] = Node('for_cond', pchildren(p))

def p_for_update(p):
    '''
    for_update : e
               | expression
    '''
    p[0] = Node('for_update', pchildren(p))

def p_for_in_block(p):
    '''
    for_in_block : FOR LPAREN AUTO IDENTIFIER IN IDENTIFIER RPAREN block
    '''
    p[0] = Node('for_in_block', pchildren(p))

def p_for_of_block(p):
    '''
    for_of_block : FOR LPAREN AUTO IDENTIFIER OF IDENTIFIER RPAREN block
    '''
    p[0] = Node('for_of_block', pchildren(p))

def p_while_block(p):
    '''
    while_block : WHILE LPAREN expression RPAREN block
    '''
    p[0] = Node('while_block', pchildren(p))

def p_do_while_block(p):
    '''
    do_while_block : DO block WHILE LPAREN expression RPAREN
    '''
    p[0] = Node('do_while_block', pchildren(p))

def p_expression(p):
    '''
    expression : LPAREN expression RPAREN
                | expression operator expression
                | unary expression
                | expression unary
                | operand
    '''
    p[0] = Node('expression', pchildren(p))

def p_operator(p):
    '''
    operator : operator_calc
             | operator_boolean
             | operator_bit
             | operator_cond
    '''
    p[0] = Node('operator', pchildren(p))

def p_operator_calc(p):
    '''
    operator_calc : PLUS
                  | MINUS
                  | MULTI
                  | DIVIDE
                  | EQUAL
                  | PLUSEQU
                  | MINUSEQU
                  | MULTIEQU
                  | DIVIDEQU
    '''
    p[0] = Node('operator_calc', pchildren(p))

def p_operator_boolean(p):
    '''
    operator_boolean : AND
                     | OR
                     | NOT
    '''
    p[0] = Node('operator_boolean', pchildren(p))

def p_operator_bit(p):
    '''
    operator_bit : BAND
                 | BOR
                 | BANDEQU
                 | BOREQU
                 | INV
    '''
    p[0] = Node('operator_bit', pchildren(p))

def p_operator_cond(p):
    '''
    operator_cond : CEQ
                  | CNEQ
                  | CGT
                  | CLT
                  | CGE
                  | CLE
    '''
    p[0] = Node('operator_cond', pchildren(p))

def p_operand(p):
    '''
    operand : IDENTIFIER
            | variable
            | IDENTIFIER LSQUARE expression RSQUARE
    '''
    p[0] = Node('operand', pchildren(p))

def p_return(p):
    '''
    return : RETURN expression
           | RETURN
    '''
    p[0] = Node('return', pchildren(p))

def p_declaration(p):
    '''
    declaration : var_type IDENTIFIER
                | var_type IDENTIFIER EQUAL expression
                | AUTO IDENTIFIER EQUAL lambda
                | var_type IDENTIFIER LSQUARE NUMBER RSQUARE
                | var_type IDENTIFIER LSQUARE NUMBER RSQUARE EQUAL expression
                | ARRAY IDENTIFIER
                | ARRAY IDENTIFIER EQUAL LBRACE RBRACE
                | ARRAY IDENTIFIER EQUAL LBRACE aggregation RBRACE
    '''
    p[0] = Node('declaration', pchildren(p))

def p_aggregation(p):
    '''
    aggregation : variable
                | variable COMMA aggregation
    '''
    p[0] = Node('aggregation', pchildren(p))

def p_unary(p):
    '''
    unary : NOT
          | INV
          | PLUSELF
          | MINUSELF
    '''
    p[0] = Node('unary', pchildren(p))

def p_variable(p):
    '''
    variable : NUMBER
             | MINUS NUMBER
             | DECIMAL
             | MINUS DECIMAL
             | CHARACTER
             | STRING
             | TRUE
             | FALSE
             | func_call
    '''
    p[0] = Node('variable', pchildren(p))

def p_func_call(p):
    '''
    func_call : IDENTIFIER LPAREN args RPAREN
              | IDENTIFIER LPAREN RPAREN
    '''
    p[0] = Node('func_call', pchildren(p))

def p_args(p):
    '''
    args : expression
         | expression COMMA args
    '''
    p[0] = Node('args', pchildren(p))


def p_lambda(p):
    '''
    lambda : LSQUARE RSQUARE LPAREN params RPAREN block
           | LPAREN params RPAREN GOTO var_type block
    '''
    p[0] = Node('lambda', pchildren(p))

def parser():
    return yacc.yacc(debug=True)