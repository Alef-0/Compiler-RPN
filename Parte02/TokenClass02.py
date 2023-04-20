from enum import Enum

class Tk_Type(Enum):
    PLUS = 1
    MINUS = 2
    TIMES = 3
    DIVISION = 4
    MODULO = 5
    NUM = 6

class Token:
    def __init__(self, token : str):
        if token.isdigit(): 
            self.type = Tk_Type.NUM
        else:
            if   token == '+': self.type = Tk_Type.PLUS
            elif token == '-': self.type = Tk_Type.MINUS
            elif token == '*': self.type = Tk_Type.TIMES
            elif token == '/': self.type = Tk_Type.DIVISION
            elif token == '%': self.type = Tk_Type.MODULO
            else: raise SyntaxError(f"UNKNOWN TOKEN: \"{token}\"")
        # No need for EOF since python always read everything

        if self.type == Tk_Type.NUM: self.lexeme = int(token)
        else: self.lexeme = token

    def __str__(self): # Overriding the print parameter
        return f"Token [type = {self.type.name}, \tlexeme = {self.lexeme}]";