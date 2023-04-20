import re

class Lexer:
        def __init__(self):
            numbers = r'[0-9]'
            symbols = r'[+-/%*]'
            self.is_num = re.compile(numbers)
            self.is_op = re.compile(symbols)