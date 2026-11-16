# Simple number converter for Mission 5

def main():
    print("Welcome to the Number Converter")
    user_input = input("Enter a positive decimal number: ")
    
    try:
        decimal_number = int(user_input)
        if decimal_number < 0:
            print("Please enter a positive number.")
            return
            
        binary_result = bin(decimal_number)
        hexadecimal_result = hex(decimal_number)
        
        print("Decimal number:", decimal_number)
        print("Binary representation:", binary_result)
        print("Hexadecimal representation:", hexadecimal_result)
        
    except ValueError:
        print("That is not a valid integer. Please enter digits only.")

if __name__ == "__main__":
    main()
