#!/usr/bin/env python3
"""
Basic Calculator
Supports: Addition, Subtraction, Multiplication, Division
"""

def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers"""
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y 

def power(x, y):
    """Raise x to the power of y"""
    return x ** y

def log(x, base=10):
    """Calculate logarithm of x with given base (default base 10)"""
    if x <= 0:
        return "Error: Logarithm undefined for non-positive numbers!"
    if base <= 0 or base == 1:
        return "Error: Invalid base for logarithm!"
    import math
    return math.log(x, base)

def main():
    """Main calculator function"""
    print("=" * 40)
    print("     BASIC CALCULATOR")
    print("=" * 40)
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power") 
    print("6. Log")    
    print("7. Exit")
    print("=" * 40)
    
    while True:
        choice = input("\nEnter choice (1/2/3/4/5/6/7): ")
        
        if choice == '7':
            print("Thank you for using the calculator!")
            break
        
        if choice in ['1', '2', '3', '4', '5', '6']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == '1':
                    print(f"\n{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"\n{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"\n{num1} × {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"\n{num1} ÷ {num2} = {result}")
                elif choice == '5':
                    result = power(num1, num2)
                    print(f"\n{num1} ** {num2} = {result}")
                elif choice == '6':
                    result = log(num1, num2)
                    print(f"\n{num1} log {num2} = {result}")   

            
            except ValueError:
                print("\nInvalid input! Please enter numbers only.")
        else:
            print("\nInvalid choice! Please select 1, 2, 3, 4, 5, 6 or 7.")

if __name__ == "__main__":
    main()