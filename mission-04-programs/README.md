# Mission 4 - How programs run

## 1. Task / objective
The objective of this mission was to write and run a simple one-line Python script from the terminal, and compare how compiled programming languages and interpreted programming languages translate and execute code.

## 2. Work completed
I created a Python file named hello.py inside the mission-04-programs directory.
Inside hello.py, I wrote a single line of Python code: print("Hello from Python").
I ran the script using the python3 command in the terminal and confirmed that the message was displayed on the screen.
I compared compilers and interpreters across four points: translation time, typical output, language examples, and main advantages.
I explained the difference between a compiler and an interpreter in simple words.

## 3. Commands / tools used
python3 mission-04-programs/hello.py: executed the Python script using the Python 3 interpreter.
cat mission-04-programs/hello.py: inspected the Python code inside the file.

## 4. My understanding

Task 4.1 - Create and run a Python program
I created hello.py with the following content:
print("Hello from Python")

When I ran it using python3 hello.py in the terminal, the terminal printed:
Hello from Python

Task 4.2 - Compare compiler and interpreter

Comparison Points:

1. When translation / execution happens:
- Compiler: Translates the entire source code file all at once before the program is executed.
- Interpreter: Translates and runs the source code line by line at runtime while the program is active.

2. Typical output:
- Compiler: Produces a separate standalone executable machine code file (like a .exe on Windows or an executable binary on macOS/Linux).
- Interpreter: Directly executes instructions immediately without saving a standalone machine code executable.

3. One example:
- Compiler: C, C++, or Rust.
- Interpreter: Python, JavaScript, or Ruby.

4. One advantage:
- Compiler: Execution speed is very fast because the program is already fully converted into machine code beforehand.
- Interpreter: Much easier for beginners to write and test code because you can quickly run the script immediately without having to do a separate compile step first.

Explanation in my own words:
A compiler reads all the source code you wrote in one go and converts it entirely into machine language before anything runs, creating an executable program file. On the other hand, an interpreter translates and executes your instructions line by line as the program is running. Because of this difference, compiled languages run faster after compiling, but interpreted languages like Python are simpler and friendlier to learn and debug because you can see errors and test changes immediately.

## 5. Difficulties faced
When I first ran python hello.py, the terminal gave a command not found error because modern macOS uses python3 instead of python.

## 6. How I resolved them
I checked my installed tools and realized I needed to type python3 hello.py. Once I used python3, the script ran immediately and displayed the message.

## 7. Evidence / files
- mission-04-programs/hello.py: Python script containing print("Hello from Python").
- mission-04-programs/README.md: documentation and comparison between compiler and interpreter.

## 8. Commit details
Commit message: Compare compilers and interpreters
Committed and pushed to GitHub repository.
