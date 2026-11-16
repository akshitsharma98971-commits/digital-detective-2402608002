# Mission 5 - Numbers and data

## 1. Task / objective
The objective of this mission was to learn how computers represent numbers and data using binary and hexadecimal, do manual conversions by hand, verify the calculations with Python functions, build a small Python converter script called number_converter.py, and learn how characters and text are stored using ASCII and UTF-8.

## 2. Work completed
I did seven math conversions by hand on paper and wrote out the step by step working for each.
I opened the Python terminal and tested each conversion using bin(), hex(), and int() to verify my manual math.
I wrote a Python program called number_converter.py that asks for a number and prints its binary and hexadecimal equivalents.
I tested number_converter.py with three different positive numbers: 13, 25, and 42.
I looked up the ASCII decimal codes for A and a, explained why computers need text encoding standards, and gave an example of a character outside of basic ASCII.

## 3. Commands / tools used
python3: ran the interactive Python shell and executed the script.
bin(): built-in Python function that converts an integer into a binary string starting with 0b.
hex(): built-in Python function that converts an integer into a hexadecimal string starting with 0x.
int(x, base): built-in Python function that converts a binary or hexadecimal string into a base-10 decimal number.

## 4. My understanding

Task 5.1 - Convert numbers by hand

1. Convert decimal 13 to binary:
Steps using repeated division by 2:
13 divided by 2 = 6 with remainder 1
6 divided by 2 = 3 with remainder 0
3 divided by 2 = 1 with remainder 1
1 divided by 2 = 0 with remainder 1
Reading remainders from bottom to top gives: 1101
Answer: 1101 in binary

2. Convert decimal 25 to binary:
Steps using repeated division by 2:
25 divided by 2 = 12 with remainder 1
12 divided by 2 = 6 with remainder 0
6 divided by 2 = 3 with remainder 0
3 divided by 2 = 1 with remainder 1
1 divided by 2 = 0 with remainder 1
Reading remainders from bottom to top gives: 11001
Answer: 11001 in binary

3. Convert binary 1010 to decimal:
Steps using positional powers of 2 (from right to left: 1, 2, 4, 8):
1 * (2 to the power 3) = 1 * 8 = 8
0 * (2 to the power 2) = 0 * 4 = 0
1 * (2 to the power 1) = 1 * 2 = 2
0 * (2 to the power 0) = 0 * 1 = 0
Total: 8 + 0 + 2 + 0 = 10
Answer: 10 in decimal

4. Convert binary 1101 to decimal:
Steps using positional powers of 2:
1 * (2 to the power 3) = 1 * 8 = 8
1 * (2 to the power 2) = 1 * 4 = 4
0 * (2 to the power 1) = 0 * 2 = 0
1 * (2 to the power 0) = 1 * 1 = 1
Total: 8 + 4 + 0 + 1 = 13
Answer: 13 in decimal

5. Convert hexadecimal A to decimal:
In base 16 (hexadecimal), single digits go from 0 to 9, then letters are used for 10 through 15:
A = 10, B = 11, C = 12, D = 13, E = 14, F = 15.
Answer: 10 in decimal

6. Convert hexadecimal 1F to decimal:
Steps using positional powers of 16 (from right to left: 1, 16):
1 * (16 to the power 1) = 1 * 16 = 16
F * (16 to the power 0) = 15 * 1 = 15
Total: 16 + 15 = 31
Answer: 31 in decimal

7. Convert binary 1111 to hexadecimal:
Steps:
1111 in binary = (1 * 8) + (1 * 4) + (1 * 2) + (1 * 1) = 8 + 4 + 2 + 1 = 15 in decimal.
In hexadecimal, the decimal value 15 is represented by the letter F.
Answer: F in hexadecimal

Task 5.2 - Verify using Python
I opened python3 in the terminal and tested the expressions:
- bin(13) returned '0b1101'. Matches my calculation.
- bin(25) returned '0b11001'. Matches my calculation.
- int('1010', 2) returned 10. Matches my calculation.
- int('1101', 2) returned 13. Matches my calculation.
- int('A', 16) returned 10. Matches my calculation.
- int('1F', 16) returned 31. Matches my calculation.
- hex(0b1111) returned '0xf'. Matches my calculation.

Task 5.3 - Build a small number converter
I wrote number_converter.py to ask the user for a number, convert it to an integer, and print its binary and hex values using bin() and hex().

Test runs performed:
Test 1:
- Input number: 13
- Binary output: 0b1101
- Hexadecimal output: 0xd

Test 2:
- Input number: 25
- Binary output: 0b11001
- Hexadecimal output: 0x19

Test 3:
- Input number: 42
- Binary output: 0b101010
- Hexadecimal output: 0x2a

What the conversion functions do:
- bin(): This built-in function takes an integer and returns its binary representation as a string with a 0b prefix, showing the bits in base 2.
- hex(): This built-in function takes an integer and returns its hexadecimal representation as a string with a 0x prefix, showing the value in base 16.

Task 5.4 - How is text stored?
1. ASCII decimal codes:
- Uppercase letter A has the ASCII code 65.
- Lowercase letter a has the ASCII code 97.

2. Why a computer needs an encoding standard to store text:
Computers are physical electronic devices that only store and process electric charges represented as 0s and 1s (bits). Because computers cannot directly store human letters, alphabets, or punctuation, they need a standardized lookup table (an encoding system) where each character is assigned a specific number code so all computers understand the same text.

3. Example of a character not in basic ASCII:
The classic ASCII standard only uses 7 bits and has 128 characters, which only covers standard English letters, numbers, and basic punctuation. Characters like the Hindi letter अ or the smiling face emoji are not in basic ASCII; they need modern UTF-8 encoding.

## 5. Difficulties faced
When doing repeated division by 2 to convert decimal to binary, I almost forgot whether to read the remainder numbers from top to bottom or bottom to top. Also, understanding why hexadecimal starts using letters like A to F took a moment to get used to.

## 6. How I resolved them
I double checked my math by multiplying the binary bits by their powers of 2 to verify they added up to the original number. Seeing that the last remainder corresponds to the largest power of 2 helped me remember to always read from bottom to top.

## 7. Evidence / files
- mission-05-numbers-data/number_converter.py: working Python script for converting numbers.
- mission-05-numbers-data/README.md: notes on manual calculations, Python verification, and text encoding.

## 8. Commit details
Commit message: Build number converter and practise data representation
Changes saved, committed, and pushed to GitHub.
