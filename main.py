import sys
from yacc import parser
from codegen import program_gen


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as infile:
        parser = parser()
        ast = parser.parse(infile.read())

    # print(program_gen(ast))

    with open(''.join(sys.argv[1].split('.')[:-1]) + '.js', 'w') as outfile:
        outfile.write(program_gen(ast))