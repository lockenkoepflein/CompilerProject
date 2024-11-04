
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
        ('NUMBER',   r'\d+(\.\d*)?'),  # Integer oder Dezimalzahl
        ('ASSIGN',   r'='),               # Zuweisungsoperator
        ('END',      r';'),               # Zeilenende
        ('ID',       r'[A-Za-z]+'),       # Bezeichner (Variablenname)
        ('OP',       r'[+\-*/]'),        # Arithmetische Operatoren
        ('WHITESPACE', r'[ \t]+'),       # Leerzeichen (ignoriert)
        ('NEWLINE',  r'\n'),             # Neue Zeile
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
    """
    Klasse für binäre Operationen (z.B. Addition, Subtraktion).
    
    Attribute:
        left (AST): Linkes Operand.
        op (str): Operator ('+', '-', '*', '/').
        right (AST): Rechtes Operand.
    """
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Num(AST):
    """
    Klasse für Zahlen im AST.
    
    Attribute:
        value (float): Der numerische Wert.
    """
    def __init__(self, value):
        self.value = value

class Assign(AST):
    """
    Klasse für Zuweisungen im AST.
    
    Attribute:
        var (str): Variablenname.
        expr (AST): Ausdruck, der der Variablen zugewiesen wird.
    """
    def __init__(self, var, expr):
        self.var = var
        self.expr = expr


# Parser: Erstellt einen AST aus Tokens
def parse(tokens):
    """
    Parser-Funktion, die eine Liste von Tokens in einen Abstract Syntax Tree (AST) umwandelt.
    
    Parameter:
        tokens (list): Liste der Tokens, die vom Lexer generiert wurden.

    Returns:
        AST: Der Root-Knoten des AST, der den Code repräsentiert.
    """
    it = iter(tokens)
    token = next(it, None)

    def eat(expected_type):
        """
        Verarbeitet ein Token des erwarteten Typs und geht zum nächsten Token über.
        
        Parameter:
            expected_type (str): Der erwartete Token-Typ.

        Returns:
            tuple: Das verarbeitete Token.

        Raises:
            SyntaxError: Falls der erwartete Token-Typ nicht übereinstimmt.
        """
        nonlocal token
        if token and token[0] == expected_type:
            old_token = token
            token = next(it, None)
            return old_token
        else:
            raise SyntaxError(f"Expected {expected_type}")

    def expr():
        """
        Funktion zur Analyse arithmetischer Ausdrücke.
        
        Returns:
            AST: Knoten im AST, der den arithmetischen Ausdruck repräsentiert.
        """
        left = term()
        while token and token[0] == 'OP':
            op = eat('OP')
            right = term()
            left = BinOp(left, op[1], right)
        return left

    def term():
        """
        Funktion zur Analyse eines Terms (eine Zahl oder eine Variable).
        
        Returns:
            AST: Knoten im AST, der den Term repräsentiert.
        """
        if token[0] == 'NUMBER':
            value = eat('NUMBER')
            return Num(float(value[1]))
        elif token[0] == 'ID':
            return eat('ID')

    def assignment():
        """
        Funktion zur Analyse einer Zuweisung (z.B. x = 5;).
        
        Returns:
            AST: Knoten im AST, der die Zuweisung repräsentiert.
        """
        var = eat('ID')
        eat('ASSIGN')
        value = expr()
        eat('END')
        return Assign(var[1], value)

    return assignment()


# Interpreter-Klasse
class Interpreter:
    """
    Interpreter-Klasse, die den AST auswertet und die Ergebnisse speichert.

    Attribute:
        variables (dict): Speichert die Werte der Variablen.
    """
    def __init__(self):
        self.variables = {}

    def visit(self, node):
        """
        Wertet einen Knoten des AST rekursiv aus.
        
        Parameter:
            node (AST): Der zu bewertende Knoten.

        Returns:
            float: Der Wert des Knotens oder None für Zuweisungen.
        """
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


# Beispiel
if __name__ == "__main__":
    code = input("Gib den Code ein, den du ausführen möchtest (z. B. 'x = 10 * 3;'): ")
    tokens = lexer(code)
    print("Tokens:", tokens)
    ast = parse(tokens)
    print("AST:", ast)
    interpreter = Interpreter()
    interpreter.visit(ast)
    print(f"Wert von x: {interpreter.variables.get('x')}")
