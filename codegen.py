import re

indentation = 0

def terminator_gen(ast):
    return str(ast)

def program_gen(ast):
    code = "const readlineSync = require('readline-sync')\n\n"

    if ast.children[0].type == 'empty':
        return code
    code += functions_gen(ast.children[0])
    code += '\nmain()\n'

    return code

def functions_gen(ast):
    if ast.children[0].type == 'function':
        code = function_gen(ast.children[0])
    elif ast.children[0].type == 'declaration':
        code = declaration_gen(ast.children[0])

    if len(ast.children) == 1:
        return code
    elif  len(ast.children) > 1:
        code += '\n'
        code += functions_gen(ast.children[1])

    return code

def function_gen(ast):
    code = 'function ' + terminator_gen(ast.children[1]) + '('
    if len(ast.children) == 6:
        code += params_gen(ast.children[3])
    code += ') '
    code += block_gen(ast.children[-1]) + '\n'

    return code

def params_gen(ast):
    code = param_gen(ast.children[0])
    if len(ast.children) == 1:
        return code
    elif  len(ast.children) > 1:
        code += ', '
        code += params_gen(ast.children[2])

    return code

def param_gen(ast):
    code = terminator_gen(ast.children[1])

    return code

def block_gen(ast):
    global indentation
    indentation += 2

    code = '{\n'
    if ast.children[1].type == 'statements':
        code += statements_gen(ast.children[1])
    code += ' ' * (indentation - 2) + '} '

    indentation -= 2

    return code

def statements_gen(ast):
    code = statement_gen(ast.children[0])
    if len(ast.children) == 1:
        return code
    elif len(ast.children) > 1:
        code += statements_gen(ast.children[1])

    return code

def statement_gen(ast):
    global indentation
    code = ' ' * indentation
    if not hasattr(ast.children[0], 'type'):
        code += terminator_gen(ast.children[0])
    elif ast.children[0].type == 'return':
        code += return_gen(ast.children[0])
    elif ast.children[0].type == 'declaration':
        code += declaration_gen(ast.children[0])
    elif ast.children[0].type == 'expression':
        code += expression_gen(ast.children[0])
    elif ast.children[0].type == 'for_block':
        code += for_block_gen(ast.children[0])
    elif ast.children[0].type == 'while_block':
        code += while_block_gen(ast.children[0])
    elif ast.children[0].type == 'do_while_block':
        code += do_while_block_gen(ast.children[0])
    elif ast.children[0].type == 'if_block':
        code += if_block_gen(ast.children[0])
    elif ast.children[0].type == 'switch_block':
        code += switch_block_gen(ast.children[0])
    elif ast.children[0].type == 'lambda_call':
        code += lambda_call_gen(ast.children[0])

    return code + '\n'

def switch_block_gen(ast):
    global indentation
    indentation += 2

    code = 'switch('
    code += expression_gen(ast.children[2])
    code += ') {\n' + ' ' * indentation

    code += case_blocks_gen(ast.children[5])
    code += '\n' + ' ' * (indentation - 2) + '}'

    indentation -= 2

    return code

def case_blocks_gen(ast):
    if ast.children[0].type == 'empty':
        return ''
    elif ast.children[0].type == 'default_block':
        code = default_block_gen(ast.children[0])
    elif ast.children[0].type == 'case_block':
        code = case_block_gen(ast.children[0])

    if len(ast.children) > 1:
        code += case_blocks_gen(ast.children[1])

    return code

def case_block_gen(ast):
    code = 'case '
    code += expression_gen(ast.children[1])
    code += ': '
    code += block_gen(ast.children[3])

    return code

def default_block_gen(ast):
    code = 'default '
    code += ': '
    code += block_gen(ast.children[2])

    return code

def if_block_gen(ast):
    code = 'if('
    code += expression_gen(ast.children[2])
    code += ') '
    code += block_gen(ast.children[4])
    code += elif_blocks_gen(ast.children[5])

    return code

def elif_blocks_gen(ast):
    if ast.children[0].type == 'empty':
        return ''
    elif ast.children[0].type == 'else_block':
        code = else_block_gen(ast.children[0])
    elif ast.children[0].type == 'elif_block':
        code = elif_block_gen(ast.children[0])
    if len(ast.children) > 1:
        code += elif_blocks_gen(ast.children[1])

    return code

def elif_block_gen(ast):
    code = 'else if('
    code += expression_gen(ast.children[3])
    code += ') '
    code += block_gen(ast.children[5])

    return code

def else_block_gen(ast):
    code = 'else '
    code += block_gen(ast.children[1])

    return code

def for_block_gen(ast):
    code = 'for('
    code += for_init_gen(ast.children[2])
    code += '; '
    code += for_cond_gen(ast.children[4])
    code += '; '
    code += for_update_gen(ast.children[6])
    code += ') '
    if ast.children[8].type == 'block':
        code += block_gen(ast.children[8])

    return code

def for_init_gen(ast):
    if ast.children[0].type == 'empty':
        code = ''
    elif ast.children[0].type == 'declaration':
        code = declaration_gen(ast.children[0])
    elif ast.children[0].type == 'expression':
        code = expression_gen(ast.children[0])

    return code

def for_cond_gen(ast):
    if ast.children[0].type == 'empty':
        code = ''
    elif ast.children[0].type == 'expression':
        code = expression_gen(ast.children[0])

    return code

def for_update_gen(ast):
    if ast.children[0].type == 'empty':
        code = ''
    elif ast.children[0].type == 'expression':
        code = expression_gen(ast.children[0])

    return code

def while_block_gen(ast):
    code = 'while('
    code += expression_gen(ast.children[2])
    code += ') '
    if (ast.children[4].type == 'block'):
        code += block_gen(ast.children[4])

    return code

def do_while_block_gen(ast):
    code = 'do'
    code += block_gen(ast.children[1])
    code += 'while ('
    code += while_cond_gen(ast.children[4])
    code += ') '

    return code

def return_gen(ast):
    code = 'return '

    if len(ast.children) == 1:
        return code
    code += expression_gen(ast.children[1])

    return code

def declaration_gen(ast):
    code = 'let '
    identifier = terminator_gen(ast.children[1])
    code += identifier

    if len(ast.children) <= 3:
        if terminator_gen(ast.children[0]) == 'array':
            code += ' = new Array()'
        return code

    if len(ast.children) < 5:
        code += ' = ' + expression_gen(ast.children[3])
    elif len(ast.children) == 5:
        code += ' = new Array()'
    elif len(ast.children) == 6:
        if terminator_gen(ast.children[0]) == 'array':
            code += ' = ['
            code += aggregation_gen(ast.children[4])
            code += ']'
        else:  # lambda
            code += ' = ('
            code += lambda_gen(ast.children[4])
            code += ')'
    elif len(ast.children) == 7:
        code += ' = new Array()'
        str = expression_gen(ast.children[6])
        if str[0] == '"' and str[-1] == '"':
            code += assign_array_gen(identifier, str[1: -1])

    return code


def lambda_call_gen(ast):
    code = '('
    code += lambda_gen(ast.children[1])
    code += ')'
    code += '('
    if len(ast.children) == 6:
        code += args_gen(ast.children[4])
    code += ')'
    return code


def lambda_gen(ast):
    code = '('
    if len(ast.children) == 5:
        code += params_gen(ast.children[1])
    code += ') => '
    code += block_gen(ast.children[-1])
    return code

def aggregation_gen(ast):
    code = variable_gen(ast.children[0])
    if len(ast.children) == 1:
        return code
    elif len(ast.children) > 1:
        code += ', '
        code += aggregation_gen(ast.children[2])

    return code

def expression_gen(ast):
    code = ''
    for child in ast.children:
        if not hasattr(child, 'type'):
            code += terminator_gen(child)
        elif child.type == 'operand':
            code += operand_gen(child)
        elif child.type == 'operator':
            code += operator_gen(child)
        elif child.type == 'expression':
            code += expression_gen(child)
        elif child.type == 'unary':
            code += unary_gen(child)

    return code

def operator_gen(ast):
    if ast.children[0].type == 'operator_calc':
        code = operator_calc_gen(ast.children[0])
    elif ast.children[0].type == 'operator_boolean':
        code = operator_boolean_gen(ast.children[0])
    elif ast.children[0].type == 'operator_cond':
        code = operator_cond_gen(ast.children[0])
    elif ast.children[0].type == 'operator_bit':
        code = operator_bit_gen(ast.children[0])

    return code

def operator_calc_gen(ast):
    return terminator_gen(ast.children[0])

def operator_boolean_gen(ast):
    return terminator_gen(ast.children[0])

def operator_cond_gen(ast):
    return terminator_gen(ast.children[0])

def operator_bit_gen(ast):
    return terminator_gen(ast.children[0])

def operand_gen(ast):
    if not hasattr(ast.children[0], 'type'):
        code = terminator_gen(ast.children[0])
        if len(ast.children) > 1:
            code += '[' + expression_gen(ast.children[2]) + ']'
    elif ast.children[0].type == 'variable':
        code = variable_gen(ast.children[0])

    return code

def unary_gen(ast):
    return terminator_gen(ast.children[0])

def variable_gen(ast):
    code = ''

    if not hasattr(ast.children[0], 'type'):
        for child in ast.children:
            code += terminator_gen(child)
    elif ast.children[0].type == 'func_call':
        return func_call_gen(ast.children[0])

    return code

def func_call_gen(ast):
    func_name = terminator_gen(ast.children[0])
    code = func_name + '('

    if len(ast.children) == 4:
        code += args_gen(ast.children[2])
    code += ')'

    if func_name == 'printf':
        code = print_gen(code)
    elif func_name == 'gets':
        code = gets_gen(code)
    elif func_name == 'strlen':
        code = strlen_gen(code)
    elif func_name == 'lenA':
        code = arraylen_gen(code)

    return code

def args_gen(ast):
    code = expression_gen(ast.children[0])
    if len(ast.children) == 1:
        return code
    elif len(ast.children) > 1:
        code += ', '
        code += args_gen(ast.children[2])

    return code

def print_gen(code):
    pattern = re.findall(r'printf\("(.*)"([^\)]*)\)', code)[0]
    code = 'process.stdout.write(`'
    if pattern[1] == '':
        code += pattern[0]
    else:
        args = pattern[1].split(',')[1:]
        p = re.sub(r'%.', '%', pattern[0])
        p_list = p.split('%')

        code += p_list[0]
        for index, arg in enumerate(args):
            code += '${' + arg.strip() + '}' + p_list[index+1]

    code += '`)'

    return code

def gets_gen(code):
    result = re.findall(r'gets\((.*)\)', code)[0]

    # change to char array
    code = result + ' = ' + "readlineSync.question('').split('').concat('\\0')"

    return code

def strlen_gen(code):
    result = re.findall(r'strlen\((.*)\)', code)[0]
    # string store in a javascript array
    # like ['H', 'e', 'l', 'l', 'o', '\0']
    # so strlen(s) = array.length - 1
    code = result + '.length-1'

    return code

def arraylen_gen(code):   
    result = re.findall(r'lenA\((.*)\)', code)[0]
    code = result + '.length'

    return code

def assign_array_gen(identifier, value):
    global indentation
    array_str = '['
    for i in value:
        array_str += "'" + i + "',"
    array_str += "'\\0']"
    code = '\n' + ' ' * indentation + identifier + ' = ' + array_str + '\n'

    return code