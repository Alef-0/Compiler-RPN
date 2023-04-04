import os.path as pt
import sys

local = pt.dirname(__file__)

def read_file(input_file = "input.txt") -> list[str]:
    # Check if it was passed a "-input" flag
    new_file = [new for new in sys.argv if ("-input=" in new)]
    if new_file: input_file = new_file[0].split("=")[-1]

    file = open(pt.join(local,input_file),"r")
    text = file.read()
    return text.split()

def solve(tokens : list[str]):
    stack = []  # I'll use python list as stacks

    for tk in tokens:
        if tk.isnumeric(): stack.append(int(tk))
        else:
            match tk:
                case '+': result = stack.pop() + stack.pop()
                case '-': result = stack.pop() - stack.pop()
                case '/': result = stack.pop() / stack.pop()
                case '%': result = stack.pop() % stack.pop()
                case '*': result = stack.pop() * stack.pop()
                case _: raise Exception(f"Unknown symbol {tk}")
            stack.append(result)

    return stack.pop()

tokens = read_file(); print(tokens)
resultado = solve(tokens)
print(f'O resultado das operações foram: {resultado}')