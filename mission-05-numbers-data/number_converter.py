"""
Digital Detective - Mission 5: Number Systems and Data Representation
number_converter.py: Converts a user-provided decimal integer to binary and hexadecimal.
"""

def main():
    print("=" * 48)
    print("       DIGITAL DETECTIVE NUMBER CONVERTER       ")
    print("=" * 48)
    
    try:
        user_input = input("Enter a positive decimal number: ").strip()
        decimal_val = int(user_input)
        
        if decimal_val < 0:
            print("Please enter a positive decimal number.")
            return

        # Python built-in conversions
        binary_str = bin(decimal_val)          # returns format '0b...'
        hex_str = hex(decimal_val).upper()     # returns format '0X...'
        
        # Formatted output displaying both raw and standard notation
        print("\n--- Conversion Results ---")
        print(f"Decimal Value     : {decimal_val}")
        print(f"Binary (Base 2)   : {binary_str} (Digits: {binary_str[2:]})")
        print(f"Hexadecimal (16)  : {hex_str.replace('0X', '0x')} (Digits: {hex_str[2:]})")
        print("-" * 48)
        
    except ValueError:
        print("Invalid input! Please enter a valid decimal integer.")

if __name__ == "__main__":
    main()
