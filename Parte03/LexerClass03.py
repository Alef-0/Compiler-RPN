import re

class Lexer:
    def __init__(self):
        #(^) is the start of line and ($) the end.
        numbers = r'^[0-9]+$'
        symbols = r'^[+-/%*]$'
        self.check_num = re.compile(numbers).fullmatch
        self.check_op = re.compile(symbols).fullmatch

    def is_num(self, token : str):
        answer = self.check_num(token)
        # print(answer)
        return answer

    def is_op(self, token : str):
        answer = self.check_op(token)
        # print(answer)
        return answer