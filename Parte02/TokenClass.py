class Token:
    def __init__(self, token : str):
        if (token is int) or token.isnumeric(): 
            self.type : str = "NUM"
        else:
            match token:
                case '+': self.type = "PLUS"
                case '-': self.type = "MINUS"
                case '*': self.type = "TIMES"
                case '/': self.type = "DIVISION"
                case '%': self.type = "MODULO"
                case _: raise Exception(f"UNKNOWN TOKEN: \"{token}\"")
        # No need for EOF since python always read everything

        if self.type == "NUM": self.lexeme = int(token)
        else: self.lexeme = token

    def __str__(self): # Overriding the print parameter
        return f"Token [type = {self.type}, \tlexeme = {self.lexeme}]";