import os.path as pt
import sys
from TokenClass import *

local = pt.dirname(__file__)

def read_file(input_file = "input.txt") -> list[str]:
    # Check if it was passed a "-input" flag
    new_file = [new for new in sys.argv if ("-input=" in new)]
    if new_file: input_file = new_file[0].split("=")[-1]

    file = open(pt.join(local,input_file),"r")
    text = file.read()
    return text.split()

def tokenize(tokens : list[str]) -> list[Token]:
    new_tokens = []
    for tk in tokens:
        new_tk = Token(tk)
        print(new_tk)
        new_tokens.append(new_tk)

    return new_tokens

def solve(tokens : list[Token]) -> Token:
    stack : list[Token] = []  # I'll use python list as stacks

    for tk in tokens:
        if tk.type == "NUM": stack.append(tk)
        else:
            match tk.type:
                case 'PLUS':    result = stack.pop().lexeme + stack.pop().lexeme
                case 'MINUS':   result = stack.pop().lexeme - stack.pop().lexeme
                case 'DIVISION':result = stack.pop().lexeme / stack.pop().lexeme
                case 'MODULO':  result = stack.pop().lexeme % stack.pop().lexeme
                case 'TIMES':   result = stack.pop().lexeme * stack.pop().lexeme
                case _: raise Exception(f"Unknown symbol {tk}")
            stack.append(Token(str(result)))

    return stack.pop()

tokens = read_file(); print(tokens)
tokenizeds = tokenize(tokens)

resultado = solve(tokenizeds)
print(f'O resultado das operações foram: {resultado.lexeme}')