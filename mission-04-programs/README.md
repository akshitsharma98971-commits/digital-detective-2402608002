# Mission 4 — How programs run

## 1. Task / objective
The objective of Mission 4 is to explore program execution mechanisms by creating and running an initial Python script, and to thoroughly analyze the architectural and operational differences between compilers and interpreters.

## 2. Work completed
- Authored a Python script named `hello.py` inside `mission-04-programs/`.
- Executed the script from the Terminal using the Python 3 runtime environment and confirmed the console output.
- Analyzed the translation pipeline, execution timing, output artifacts, examples, and advantages of compiled versus interpreted languages.
- Documented findings in `mission-04-programs/README.md`.

---

## 3. Commands / tools used
| Tool / Command | Purpose | Output / Observation |
| :--- | :--- | :--- |
| `python3 hello.py` | Execute the Python script using the CPython 3 interpreter | Printed `Hello from Python` to standard output. |
| `python3 --version` | Verify the Python interpreter version | `Python 3.9.6` |

---

## 4. My understanding

### Task 4.1 — Python Program Execution
The file `hello.py` was created containing:
```python
print("Hello from Python")
```
When executed in Terminal via `python3 hello.py`, the Python interpreter parsed the syntax, translated the instruction into intermediate bytecode, evaluated the bytecode on the Python Virtual Machine (PVM), and dispatched the string to standard output, displaying:
```
Hello from Python
```

---

### Task 4.2 — Compare compiler and interpreter

| Point | Compiler | Interpreter |
| :--- | :--- | :--- |
| **When translation / execution happens** | Translation happens entirely in advance (before execution). Source code is translated in full into machine code before any execution starts. | Translation happens dynamically at runtime. Instructions or statements are translated and executed line-by-line or chunk-by-chunk while the program is running. |
| **Typical output** | Standalone native binary machine code executable (e.g. `.exe`, ELF binary, Mach-O binary) or object files (`.o`). | Direct runtime execution results in memory, or transient intermediate bytecode (e.g. `.pyc` files) fed directly into a virtual runtime. |
| **One example** | **C** / **C++** (using `gcc` or `clang`), **Rust** (`rustc`), **Go**. | **Python** (`python3`), **JavaScript** (browser engines / Node.js), **Ruby**. |
| **One advantage** | Maximum execution speed and efficiency. Because code is translated and optimized ahead of time directly for target CPU instructions, it runs without translation overhead at runtime. | Rapid development, flexibility, and platform independence. Developers can test and run scripts immediately without lengthy compilation cycles, making debugging more accessible. |

#### Comprehensive Explanation:
A compiler translates high-level human-readable source code into native machine code instructions in an advance compilation stage before the program can ever be executed. Once compiled, the resulting binary executable runs directly on the CPU hardware with exceptional performance and optimization.

In contrast, an interpreter processes source code or intermediate bytecode line-by-line at runtime, executing instructions on the fly without producing a separate machine-code binary. While interpreters incur runtime translation overhead, they enable immediate execution feedback, dynamic typing, and frictionless cross-platform portability. Notably, modern language environments often blend both techniques—such as Python compiling source code into bytecode before interpreting it within the Python Virtual Machine (PVM).

---

## 5. Difficulties faced
- Conceptualizing how Python sits between a pure interpreter and a compiler due to its internal generation of `.pyc` bytecode files.

## 6. How I resolved them
- Explored CPython's execution model and noted that while Python compiles source into intermediate bytecode, execution is handled at runtime by an interpreter loop, classifying it primarily as an interpreted language environment for the user.

## 7. Evidence / files
- Python program: `mission-04-programs/hello.py`
- Documentation: `mission-04-programs/README.md`

## 8. Commit details
- **Commit Message:** `Compare compilers and interpreters`
- **Pushed to GitHub:** Yes (Branch: `main`)
