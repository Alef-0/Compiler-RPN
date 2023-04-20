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

def scan(tokens : list[str]) -> list[Token]:
    new_tokens = []
    for tk in tokens:
        new_tk = Token(tk)
        print(new_tk)
        new_tokens.append(new_tk)

    return new_tokens

def solve(tokens : list[Token]) -> Token:
    stack : list[Token] = []  # I'll use python list as stacks

    for tk in tokens:
        if tk.type == Tk_Type.NUM: stack.append(tk)
        else:
            if   tk.type == Tk_Type.PLUS:     result = stack.pop().lexeme + stack.pop().lexeme
            elif tk.type == Tk_Type.MINUS:    result = stack.pop().lexeme - stack.pop().lexeme
            elif tk.type == Tk_Type.DIVISION: result = stack.pop().lexeme / stack.pop().lexeme
            elif tk.type == Tk_Type.MODULO:   result = stack.pop().lexeme % stack.pop().lexeme
            elif tk.type == Tk_Type.TIMES:    result = stack.pop().lexeme * stack.pop().lexeme
            else: raise SyntaxError(f"Unknown symbol {tk}")
            stack.append(Token(str(result)))

    return stack.pop()

symbols : list[str] = read_file(); print(symbols) # Read File
tokens : list[Token] = scan(symbols)

resultado = solve(tokens)
print(f'O resultado das operações foram: {resultado.lexeme}')