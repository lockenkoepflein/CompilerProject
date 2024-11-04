
import re

# Lexer: Zerlegt den Code in Tokens
def lexer(code):
    """
    Lexer-Funktion, die den Quellcode in eine Liste von Tokens umwandelt.
    Ein Token ist eine eindeutige Einheit (wie Schlüsselwörter, Variablennamen, Operatoren etc.).
    
    Parameter:
        code (str): Der Quellcode, der lexikalisch analysiert werden soll.

    Returns:
        list: Eine Liste von Tokens, jedes Token ist ein Tupel aus (Token-Typ, Wert).
    """
    tokens = []
    token_specification = [
        ('COMMAND', r'\b(PRINT|SET|ADD|SUB)\b'),  # Befehle wie PRINT, SET, ADD, SUB
        ('NUMBER',   r'\d+(\.\d*)?'),            # Integer oder Dezimalzahl
        ('ASSIGN',   r'='),                         # Zuweisungsoperator
        ('END',      r';'),                         # Zeilenende
        ('ID',       r'[A-Za-z]+'),                 # Bezeichner (Variablenname)
        ('OP',       r'[+\-*/]'),                  # Arithmetische Operatoren
        ('WHITESPACE', r'[ \t]+'),                 # Leerzeichen (ignoriert)
        ('NEWLINE',  r'\n'),                       # Neue Zeile
    ]
    token_re = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    for match in re.finditer(token_re, code):
        token_type = match.lastgroup
        value = match.group()
        if token_type != 'WHITESPACE':  # Ignoriere Leerzeichen
            tokens.append((token_type, value))
    return tokens


# Abstract Syntax Tree (AST) Klassen
class AST:
    """Basisklasse für alle Knoten im Abstract Syntax Tree (AST)."""
    pass

class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Num(AST):
    def __init__(self, value):
        self.value = value

class Assign(AST):
    def __init__(self, var, expr):
        self.var = var
        self.expr = expr

class PrintCommand(AST):
    def __init__(self, var):
        self.var = var

class AddCommand(AST):
    def __init__(self, var, value):
        self.var = var
        self.value = value

class SubCommand(AST):
    def __init__(self, var, value):
        self.var = var
        self.value = value


# Parser: Erstellt einen AST aus Tokens
def parse(tokens):
    it = iter(tokens)
    token = next(it, None)

    def eat(expected_type):
        nonlocal token
        if token and token[0] == expected_type:
            old_token = token
            token = next(it, None)
            return old_token
        else:
            raise SyntaxError(f"Expected {expected_type}")

    def expr():
        left = term()
        while token and token[0] == 'OP':
            op = eat('OP')
            right = term()
            left = BinOp(left, op[1], right)
        return left

    def term():
        if token[0] == 'NUMBER':
            value = eat('NUMBER')
            return Num(float(value[1]))
        elif token[0] == 'ID':
            return eat('ID')

    def assignment():
        var = eat('ID')
        eat('ASSIGN')
        value = expr()
        eat('END')
        return Assign(var[1], value)

    def command():
        cmd_token = eat('COMMAND')
        if cmd_token[1] == 'PRINT':
            var = eat('ID')
            eat('END')
            return PrintCommand(var[1])
        elif cmd_token[1] == 'SET':
            var = eat('ID')
            eat('ASSIGN')
            value = expr()
            eat('END')
            return Assign(var[1], value)
        elif cmd_token[1] == 'ADD':
            var = eat('ID')
            value = expr()
            eat('END')
            return AddCommand(var[1], value)
        elif cmd_token[1] == 'SUB':
            var = eat('ID')
            value = expr()
            eat('END')
            return SubCommand(var[1], value)

    if token[0] == 'COMMAND':
        return command()
    else:
        return assignment()


# Interpreter-Klasse
class Interpreter:
    def __init__(self):
        self.variables = {}

    def visit(self, node):
        if isinstance(node, Num):
            return node.value
        elif isinstance(node, BinOp):
            left = self.visit(node.left)
            right = self.visit(node.right)
            if node.op == '+':
                return left + right
            elif node.op == '-':
                return left - right
            elif node.op == '*':
                return left * right
            elif node.op == '/':
                return left / right
        elif isinstance(node, Assign):
            value = self.visit(node.expr)
            self.variables[node.var] = value
            return value
        elif isinstance(node, PrintCommand):
            print(f"Wert von {node.var}: {self.variables.get(node.var, 'undefiniert')}")
        elif isinstance(node, AddCommand):
            self.variables[node.var] += self.visit(node.value)
        elif isinstance(node, SubCommand):
            self.variables[node.var] -= self.visit(node.value)


# Beispiel
if __name__ == "__main__":
    code = input("Gib den Code ein, den du ausführen möchtest (z. B. 'SET x = 10; ADD x 5; PRINT x;'): ")
    tokens = lexer(code)
    print("Tokens:", tokens)
    ast = parse(tokens)
    print("AST:", ast)
    interpreter = Interpreter()
    interpreter.visit(ast)
