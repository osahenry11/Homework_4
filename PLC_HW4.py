class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.index = -1
        self.advance()

    def advance(self):
        # Increments the index and then sets the current token to the next token 
        self.index += 1
        if self.index < len(self.tokens):
            self.current_token = self.tokens[self.index]
        else:
            self.current_token = None

    def match(self, token_type):
        # Check to see  if the current token matches the expected token type
        # advance , if not raise exception 
        if self.current_token and self.current_token.type == token_type:
            self.advance()
        else:
            raise Exception(f"Syntax error: Expected {token_type} but found {self.current_token.type}")

    def parse(self):

        self.stmt_list()

    def stmt_list(self):
        self.stmt()
        self.match(';')
        # Keep calling the statement function and matching semicolons until we reach the end of the statement list
        while self.current_token and self.current_token.type != '}':
            self.stmt()
            self.match(';')

    def stmt(self):
        # Determinining  which statement function to call in accordanxce to their  current token
        if self.current_token.type == 'IF':
            self.if_stmt()
        elif self.current_token.type == '{':
            self.block()
        elif self.current_token.type == 'WHILE':
            self.while_loop()
        else:
            self.expr()

    def if_stmt(self):
        self.match('IF')
        self.match('(')
        self.bool_expr()
        self.match(')')
        # If the next token is a left brace, call the block function and check for an "else" statement
        if self.current_token.type == '{':
            self.block()
            if self.current_token and self.current_token.type == 'ELSE':
                self.match('ELSE')
                # If the next token is a left brace, call the block function; otherwise, call the statement function
                if self.current_token.type == '{':
                    self.block()
                else:
                    self.stmt()
        # If the next token is not a left brace, call the statement function and check for an "else" statement
        else:
            self.stmt()
            if self.current_token and self.current_token.type == 'ELSE':
                self.match('ELSE')
                # If the next token is a left brace, call the block function; otherwise, call the statement function
                if self.current_token.type == '{':
                    self.block()
                else:
                    self.stmt()

    def block(self):
        self.match('{')
        self.stmt_list()
        self.match('}')




    def while_loop(self):
        # Matching  the "while" keyword, the left parenthesis, and the boolean expression
        self.match('WHILE')
        self.match('(')
        self.bool_expr()
        self.match(')')
        if self.current_token.type == '{':
            self.block()
        else

  def expr(self):
        self.term()
        while self.current_token and self.current_token.type in ['+', '-']:
            op = self.current_token
            self.advance()
            self.term()

    def term(self):
        self.factor()
        while self.current_token and self.current_token.type in ['*', '/', '%']:
            op = self.current_token
            self.advance()
            self.factor()

    def factor(self):
        if self.current_token.type == 'ID':
            self.match('ID')
        elif self.current_token.type in ['INT_LIT', 'FLOAT_LIT']:
            self.match(self.current_token.type)
        elif self.current_token.type == '(':
            self.match('(')
            self.expr()
            self.match(')')

    def bool_expr(self):
        self.bterm()
        while self.current_token and self.current_token.type in ['>', '<', '>=', '<=']:
            op = self.current_token
            self.advance()
            self.bterm()

    def bterm(self):
        self.band()
        while self.current_token and self.current_token.type in ['==', '!=']:
            op = self.current_token
            self.advance()
            self.band()

    def band(self):
        self.bor()
        while   

