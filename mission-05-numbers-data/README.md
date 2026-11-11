# Mission 5 — Numbers and data

## 1. Task / objective
The objective of Mission 5 is to understand fundamental data representation inside computer architectures: performing manual step-by-step conversions between decimal (Base 10), binary (Base 2), and hexadecimal (Base 16) number systems, verifying calculations with Python functions, engineering an interactive Python CLI conversion tool (`number_converter.py`), and analyzing text encoding standards (ASCII vs. Unicode/UTF-8).

## 2. Work completed
- Performed step-by-step manual conversions for all 7 required numeric problems (showing division-by-2 remainder methods, positional power expansion, and hex nibble conversions).
- Verified each conversion using Python's built-in functions in interactive testing (`bin()`, `hex()`, `int()`, `ord()`).
- Programmed a robust command-line conversion application: `number_converter.py`.
- Tested the converter with diverse positive integers (13, 25, 42, 255) and documented the outputs.
- Answered theoretical questions on character encoding, ASCII byte values, and Unicode UTF-8 representations.
- Documented findings in `mission-05-numbers-data/README.md`.

---

## 3. Commands / tools used
| Function / Command | Purpose | Example Tested | Result |
| :--- | :--- | :--- | :--- |
| `bin(n)` | Converts a decimal integer into a binary string prefixed with `0b` | `bin(13)` | `'0b1101'` |
| `hex(n)` | Converts a decimal integer into a hexadecimal string prefixed with `0x` | `hex(0b1111)` | `'0xf'` |
| `int(str, base)` | Parses an integer from a string representation in the specified radix/base | `int('1010', 2)` | `10` |
| `int(str, 16)` | Parses a hexadecimal string into base 10 integer | `int('1F', 16)` | `31` |
| `ord(char)` | Returns the integer Unicode / ASCII code point for a given character | `ord('A')` | `65` |
| `python3 number_converter.py` | Runs the interactive number conversion tool | User input test | Executed |

---

## 4. My understanding

### Task 5.1 — Convert numbers by hand

#### 1. Convert decimal 13 to binary
- Repeated division by 2, recording remainders from least significant bit (LSB) to most significant bit (MSB):
  - $13 \div 2 = 6$, remainder **1** (LSB)
  - $6 \div 2 = 3$, remainder **0**
  - $3 \div 2 = 1$, remainder **1**
  - $1 \div 2 = 0$, remainder **1** (MSB)
- Reading remainders from bottom to top: **$1101_2$**
- Verification: $(1 \times 2^3) + (1 \times 2^2) + (0 \times 2^1) + (1 \times 2^0) = 8 + 4 + 0 + 1 = 13_{10}$.

#### 2. Convert decimal 25 to binary
- Repeated division by 2:
  - $25 \div 2 = 12$, remainder **1** (LSB)
  - $12 \div 2 = 6$, remainder **0**
  - $6 \div 2 = 3$, remainder **0**
  - $3 \div 2 = 1$, remainder **1**
  - $1 \div 2 = 0$, remainder **1** (MSB)
- Reading remainders from bottom to top: **$11001_2$**
- Verification: $(1 \times 2^4) + (1 \times 2^3) + (0 \times 2^2) + (0 \times 2^1) + (1 \times 2^0) = 16 + 8 + 0 + 0 + 1 = 25_{10}$.

#### 3. Convert binary 1010 to decimal
- Positional power expansion in base 2:
  - Bit 3 ($2^3$): $1 \times 8 = 8$
  - Bit 2 ($2^2$): $0 \times 4 = 0$
  - Bit 1 ($2^1$): $1 \times 2 = 2$
  - Bit 0 ($2^0$): $0 \times 1 = 0$
  - Sum: $8 + 0 + 2 + 0 =$ **$10_{10}$**

#### 4. Convert binary 1101 to decimal
- Positional power expansion:
  - Bit 3 ($2^3$): $1 \times 8 = 8$
  - Bit 2 ($2^2$): $1 \times 4 = 4$
  - Bit 1 ($2^1$): $0 \times 2 = 0$
  - Bit 0 ($2^0$): $1 \times 1 = 1$
  - Sum: $8 + 4 + 0 + 1 =$ **$13_{10}$**

#### 5. Convert hexadecimal A to decimal
- In hexadecimal, the single digit $A$ represents decimal $10$.
- Expansion: $10 \times 16^0 =$ **$10_{10}$**

#### 6. Convert hexadecimal 1F to decimal
- Hexadecimal has base 16, where $F = 15$:
  - High nibble ($16^1$): $1 \times 16 = 16$
  - Low nibble ($16^0$): $15 \times 1 = 15$
  - Sum: $16 + 15 =$ **$31_{10}$**

#### 7. Convert binary 1111 to hexadecimal
- 4 bits (one nibble) convert directly into one hexadecimal digit:
  - Decimal value: $(1 \times 8) + (1 \times 4) + (1 \times 2) + (1 \times 1) = 8 + 4 + 2 + 1 = 15_{10}$
  - In hexadecimal, $15_{10}$ is represented by the digit **$F_{16}$** (or $0xF$).

---

### Task 5.2 — Verify using Python

| Expression Tested | Python Output | Matches Manual Calculation? |
| :--- | :--- | :---: |
| `bin(13)` | `'0b1101'` | Yes ($1101_2$) |
| `bin(25)` | `'0b11001'` | Yes ($11001_2$) |
| `int('1010', 2)` | `10` | Yes ($10_{10}$) |
| `int('1101', 2)` | `13` | Yes ($13_{10}$) |
| `int('A', 16)` | `10` | Yes ($10_{10}$) |
| `int('1F', 16)` | `31` | Yes ($31_{10}$) |
| `hex(0b1111)` | `'0xf'` | Yes ($F_{16}$) |

All Python runtime evaluations matched manual calculations with 100% precision.

---

### Task 5.3 — Small Number Converter Program
The program `number_converter.py` was created to prompt users for a positive decimal number, safely parse input as an integer, and output both binary and hexadecimal equivalents.

#### Execution Test Results:
| Test Number (Decimal) | Binary Output | Hexadecimal Output | Observation |
| :--- | :--- | :--- | :--- |
| **13** | `0b1101` (`1101`) | `0xD` (`D`) | Matches manual Task 5.1 calculations |
| **25** | `0b11001` (`11001`) | `0x19` (`19`) | Matches manual Task 5.1 calculations |
| **42** | `0b101010` (`101010`) | `0x2A` (`2A`) | Confirms multi-byte conversion ($32+8+2=42$, $2\times16 + 10 = 42$) |
| **255** | `0b11111111` (`11111111`) | `0xFF` (`FF`) | Full 8-bit byte representation |

#### Explanation of Python conversion functions:
- `bin(x)`: Converts an integer `x` into a binary string prefixed with `'0b'`. It calculates the base-2 positional bits representing the magnitude of the integer.
- `hex(x)`: Converts an integer `x` into a lowercase hexadecimal string prefixed with `'0x'`. It aggregates every 4 bits into one of the 16 hexadecimal symbols (`0-9`, `a-f`).

---

### Task 5.4 — How is text stored?
- **ASCII decimal codes:**
  - Uppercase **'A'**: Decimal **65** (Binary: `01000001`, Hex: `0x41`)
  - Lowercase **'a'**: Decimal **97** (Binary: `01100001`, Hex: `0x61`)
- **Why a computer needs an encoding standard to store text:**
  Computers cannot natively store letters, symbols, or language glyphs; physical memory hardware operates strictly on binary electrical charges (0s and 1s). An encoding standard establishes an unambiguous universal translation mapping (code table) between alphanumeric characters and specific numeric binary integers so that text can be stored, transmitted, and rendered accurately across different operating systems and devices.
- **Example of a character not in basic ASCII:**
  The Euro currency symbol **€** (Unicode code point `U+20AC`) or the Devanagari character **अ** (Unicode code point `U+0905`). Basic ASCII is strictly a 7-bit standard (values 0–127) containing only standard English letters, digits, and control characters; extended characters and international alphabets require UTF-8 multi-byte encoding.

---

## 5. Difficulties faced
- Handling the `'0b'` and `'0x'` prefixes returned by Python's built-in `bin()` and `hex()` functions when displaying pure numeric digits.

## 6. How I resolved them
- Used string slicing (`[2:]`) to show both the standard programmer notation (e.g. `0b1101`) and the raw numerical digits (`1101`) for clarity.

## 7. Evidence / files
- Python converter script: `mission-05-numbers-data/number_converter.py`
- Documentation: `mission-05-numbers-data/README.md`

## 8. Commit details
- **Commit Message:** `Build number converter and practise data representation`
- **Pushed to GitHub:** Yes (Branch: `main`)
