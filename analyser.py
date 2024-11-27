import re
from typing import List, Tuple, Union


TOKENS = [
    ("NUMEROS", r'\d+(\.\d+)?'),                  
    ("STRING", r'"[^"]*"'),                      
    ("KEYWORD", r'\b(if|else|while|return)\b'),  
    ("IDENTIFICADOR", r'[a-zA-Z_]\w*'),             
    ("OPERADOR", r'[+\-*/%]'),                   
    ("COMPARACAO", r'[<>!=]=?|=='),             
    ("ATRIBUICAO", r'='),                        
    ("PUNCTUACAO", r'[(){};,]'),                
    ("WHITESPACE", r'\s+'),                      
    ("UNKNOWN", r'.'),                           
]


def lexer(code):
    tokens = []
    position = 0

    while position < len(code):
        match = None
        for token_type, pattern in TOKENS:
            regex = re.compile(pattern)
            match = regex.match(code, position)
            if match:
                text = match.group(0)
                if token_type != "WHITESPACE":  
                    tokens.append((token_type, text))
                position = match.end()
                break

        if not match:
            raise SyntaxError(f"Token inválido no texto: {code[position]}")

    return tokens


code = '''
if (x > 10) {
    y = "Hello, World!";
    return y + 42.5;
}
'''

tokens = lexer(code)

for token in tokens:
    print(token)

