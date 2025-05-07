# 🧠 Mini-Interpreter für eine eigene Sprache in Python

Ein einfaches, aber vollständiges Projekt zur Umsetzung eines eigenen Interpreters mit **Lexer**, **Parser**, **AST** und **Interpreter-Logik** in Python.  
Die Beispielsprache unterstützt Variablen, Zuweisungen, einfache Rechenoperationen sowie `PRINT`, `SET`, `ADD`, `SUB`-Befehle.

---

## ✨ Funktionen

- 🔤 **Lexer** – erkennt Schlüsselwörter, Operatoren, Zahlen, Bezeichner, etc.
- 🌳 **Parser** – erzeugt einen Abstract Syntax Tree (AST)
- 🧮 **Interpreter** – führt Anweisungen aus und verarbeitet Variablen
- 🧾 **Syntax** wie `SET x = 5; ADD x 3; PRINT x;`

---

## 🚀 Beispiel

```text
Eingabe:
SET x = 10;
ADD x 5;
SUB x 3;
PRINT x;

Ausgabe:
Wert von x: 12.0
