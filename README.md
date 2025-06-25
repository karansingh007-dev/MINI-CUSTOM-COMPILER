🧠 MiniLang — A Simple English-like Compiler with Web IDE
MiniLang is a lightweight compiler-interpreter built using Python and PLY (Python Lex-Yacc). It supports a simple, intuitive syntax inspired by natural language to help beginners understand programming constructs like variables, expressions, loops, and conditions.

It features a responsive dark-themed frontend web IDE, integrated with a Flask backend to execute code written in MiniLang.

🚀 Features
Natural-language-inspired syntax (e.g. set x as 5;)

Variable assignments and arithmetic expressions

if-else conditions

while loops

Web-based dark mode editor

Real-time code execution

Built using Python, Flask, and PLY

🧱 Technologies Used
Component	Technology
Frontend	HTML, CSS, JavaScript
Backend	Python, Flask
Compiler	PLY (Lex + Yacc)
Integration	JavaScript fetch API
Styling	Responsive dark mode UI

🧑‍💻 Project Structure
graphql
Copy code
MiniLangProject/
├── app.py                # Flask backend (API + render frontend)
├── compiler.py           # Lexer, Parser, and Interpreter (using PLY)
├── templates/
│   └── index.html        # Web-based code editor UI
├── static/
│   └── style.css         # Optional custom CSS styling
├── README.md             # This file
✍️ Example MiniLang Code
text
Copy code
set x as 1;

while x < 4 {
    display x;
    set x as x + 1;
}

if x == 4 {
    display 100;
} else {
    display 0;
}
🖨 Output:

vbnet
Copy code
x set to 1
1
2
3
x set to 2
x set to 3
x set to 4
100
⚙️ How to Run the Project Locally
1. Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/minilang.git
cd minilang
2. Install Required Packages
bash
Copy code
pip install flask ply
3. Run the Application
bash
Copy code
python app.py
Open your browser and visit http://127.0.0.1:5000

🧪 Compiler Phases Implemented
Phase	Implemented?	Description
Lexical Analysis	✅ Yes	Tokenizes code using PLY
Syntax Analysis	✅ Yes	Validates code structure
Semantic Analysis	✅ Yes	Ensures variable rules, type safety
