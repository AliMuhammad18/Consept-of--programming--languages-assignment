import re

TOKEN_SPECIFICATION = [
    ('NUMBER',   r'\b\d+(\.\d+)?\b'),
    ('Identifier', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'), 
    ('ASSIGN',   r'='),  
    ('SEMICOLON', r';'),
    ('ADD_OP',   r'[+]'),
    ('SUB_OP',   r'[-]'),
    ('MUL_OP',   r'[*]'),
    ('DIV_OP',   r'[/]'),  
    ('LPAREN',   r'\('), 
    ('RPAREN',   r'\)'),  
    ('LBRACE',   r'\{'),
    ('RBRACE',   r'\}'), 
    ('WHITESPACE', r'\s+'),
]

def tokenize(code):
    tokens = []
    combined_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPECIFICATION)
    for match in re.finditer(combined_regex, code):
        kind = match.lastgroup
        value = match.group()
        if kind != 'WHITESPACE':  # Ignore whitespace
            tokens.append((kind, value))
    return tokens

code = "x = 42 + (y * 3.5) } {;"
tokens = tokenize(code)
for token in tokens:
    print(token)
