# 🧠 Mini Interpreter for a Custom Language in Python

A simple yet complete project implementing an interpreter with **lexer**, **parser**, **AST**, and **interpreter** components in Python.  
The custom mini-language supports variables, basic arithmetic operations, and commands like `SET`, `ADD`, `SUB`, and `PRINT`.

---

## ✨ Features

- 🔤 **Lexer**: Recognizes keywords, numbers, operators, identifiers, etc.  
- 🌳 **Parser**: Builds an Abstract Syntax Tree (AST)  
- 🧮 **Interpreter**: Executes the AST (assignment, arithmetic, output)  
- 🧾 Supports multiple instructions in a session  

---

## 🚀 Example

```
Input:
SET x = 10;
ADD x 5;
SUB x 3;
PRINT x;

Output:
Value of x: 12.0
```

---

## 📄 Supported Language Elements

| Element     | Description                                      |
|-------------|--------------------------------------------------|
| `SET`       | Assign a value to a variable (`SET x = 5;`)      |
| `ADD`       | Add a value to a variable (`ADD x 2;`)           |
| `SUB`       | Subtract a value from a variable (`SUB x 1;`)    |
| `PRINT`     | Output the value of a variable (`PRINT x;`)      |
| `+ - * /`   | Arithmetic operations within expressions          |
| `;`         | End of a statement                               |

---

## ▶️ Running the Program

```bash
python compiler.py
```

You can then enter interactive code, for example:

```
SET a = 3 + 2 * 4;
PRINT a;
```

---

## 🛠 Project Structure

```
main.py                 # Contains lexer, parser, AST, and interpreter  
README.md               # This file  
```

---

## 🎓 Background & Purpose

This project was created during my self-study as part of the **Cyber Security (B.Sc.)** program to apply concepts from **compiler construction, theoretical computer science, and language processing** in a practical way.

The goal was to model the typical stages of a programming language:

- Lexical analysis (tokenizer)
- Syntax analysis (parser + AST)
- Semantic evaluation (interpreter)

### 📌 This project is especially useful for:

- **Students** wanting to understand compiler/interpreter concepts in Python  
- **Teaching purposes**, e.g., to visualize language processing  
- **Portfolio projects**, e.g., for scholarships or job applications

The codebase is designed for easy extension (see below).

---

## 💡 Potential Extensions

- `IF` / `ELSE` / `WHILE` (control structures)  
- Logical operators (`==`, `>`, `<`, `AND`, `OR`)  
- `PRINT x + 1;` (output expressions, not just variables)  
- Support for **comments** in the source (`# ...`)  
- **Error messages with context** (line, token)  

---

## 🔒 Limitations

- No type checking (all values are `float`)  
- No functions or scoping  
- No error handling for division by zero, etc.  
- Only linear program execution (no control flow branching)  

---

## 🧑‍💻 About Me

I am a **Cyber Security (B.Sc.)** student in a part-time study program with a strong interest in **theoretical computer science, digital forensics, and compiler design**.  
This project was created to **independently deepen practical skills** in the area of language processing and serves as a portfolio example.

---

## 📄 License

This project is licensed under the **MIT License**.  
A `LICENSE` file can be added to the repository if needed.

