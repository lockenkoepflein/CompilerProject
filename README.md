# 🧠 Mini-Interpreter für eine eigene Sprache in Python

Ein einfaches, aber vollständiges Projekt zur Umsetzung eines Interpreters mit **Lexer**, **Parser**, **AST** und **Interpreter** in Python.  
Die entworfene Mini-Sprache unterstützt Variablen, einfache Rechenoperationen sowie Befehle wie `SET`, `ADD`, `SUB` und `PRINT`.

---

## ✨ Funktionen

- 🔤 **Lexer**: Erkennt Schlüsselwörter, Zahlen, Operatoren, Bezeichner etc.  
- 🌳 **Parser**: Erstellt einen Abstract Syntax Tree (AST)  
- 🧮 **Interpreter**: Führt den AST aus (Zuweisung, Rechnen, Ausgabe)  
- 🧾 Unterstützt mehrere Anweisungen in einer Sitzung  

---

## 🚀 Beispiel

```
Eingabe:
SET x = 10;
ADD x 5;
SUB x 3;
PRINT x;

Ausgabe:
Wert von x: 12.0
```

---

## 📄 Unterstützte Sprachelemente

| Element     | Beschreibung                                     |
|-------------|--------------------------------------------------|
| `SET`       | Variable setzen (`SET x = 5;`)                  |
| `ADD`       | Wert zur Variable addieren (`ADD x 2;`)         |
| `SUB`       | Wert von Variable subtrahieren (`SUB x 1;`)     |
| `PRINT`     | Ausgabe einer Variable (`PRINT x;`)             |
| `+ - * /`   | Arithmetische Operationen in Ausdrücken         |
| `;`         | Abschluss einer Anweisung                       |

---

## ▶️ Ausführen

```bash
python main.py
```

Dann kannst du den Code interaktiv eingeben, z. B.:

```
SET a = 3 + 2 * 4;
PRINT a;
```

---

## 🛠 Projektstruktur

```
main.py                 # Enthält Lexer, Parser, AST und Interpreter  
README.md               # Diese Datei  
```

---

## 🎓 Hintergrund & Verwendung

Dieses Projekt entstand im Rahmen meines Selbststudiums im Studiengang **Cyber Security (B.Sc.)** mit dem Ziel, Konzepte aus **Compilerbau, theoretischer Informatik und Sprachverarbeitung** praxisnah umzusetzen.

Ziel war es, die typischen Verarbeitungsschritte einer Programmiersprache abzubilden:

- Lexikalische Analyse (Tokenizer)
- Syntaxanalyse (Parser + AST)
- Semantische Auswertung (Interpreter)

### 📌 Das Projekt eignet sich besonders für:

- **Studierende**, die Compiler- oder Interpreterkonzepte in Python verstehen möchten  
- **Lehrzwecke**, z. B. zur Visualisierung von Sprachverarbeitung  
- **Portfolio-Projekte**, z. B. im Kontext von Stipendien oder Bewerbungen

Die Codebasis ist so gestaltet, dass **Erweiterungen einfach möglich** sind (siehe unten).

---

## 💡 Mögliche Erweiterungen

- `IF` / `ELSE` / `WHILE` (Kontrollstrukturen)  
- Logische Operatoren (`==`, `>`, `<`, `AND`, `OR`)  
- `PRINT x + 1;` (Ausdrucksausgabe statt nur Variablen)  
- Unterstützung für **Kommentare** im Quelltext (`# ...`)  
- **Fehlermeldungen mit Kontext** (Zeile, Token)  

---

## 🔒 Einschränkungen

- Keine Typprüfung (alle Werte sind `float`)  
- Keine Funktionen oder Scoping  
- Kein Fehlermanagement für Division durch 0 o. ä.  
- Nur lineare Programmausführung (keine Kontrollflussverzweigungen)  

---

## 🧑‍💻 Über mich

Ich studiere **Cyber Security (B.Sc.)** im berufsbegleitenden Studium mit großem Interesse an **theoretischer Informatik, IT-Forensik und Compilertechnik**.  
Dieses Projekt entstand zur **eigenständigen Vertiefung praktischer Fähigkeiten** im Bereich Sprachverarbeitung und soll als Portfolio-Beispiel dienen.

---

## 📄 Lizenz

Dieses Projekt steht unter der **MIT-Lizenz**.  
Eine `LICENSE`-Datei kann bei Bedarf im Repository ergänzt werden.
