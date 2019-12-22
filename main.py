import sys
from yacc import parser
from codegen import program_gen

if __name__ == '__main__':
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as infile:
            parser = parser()
            ast = parser.parse(infile.read())

        # print(program_gen(ast))

        with open(''.join(sys.argv[1].split('.')[:-1]) + '.js', 'w') as outfile:
            outfile.write(program_gen(ast))
    else:
        parser = parser()
        examples = {'calculator.c', 'palindrome.c', 'kmp.c', 'array.c', 'for_inof.c', 'lambda.c'}
        for file in examples:
            with open(file, 'r') as infile:

                ast = parser.parse(infile.read())

                # print(program_gen(ast))

                with open(''.join(file.split('.')[:-1]) + '.js', 'w') as outfile:
                    outfile.write(program_gen(ast))
