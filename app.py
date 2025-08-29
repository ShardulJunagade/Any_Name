"""
Simple calculator module providing basic arithmetic functions and a CLI.

Functions:
- add(x, y): Return the sum of two numbers.
- subtract(x, y): Return the difference of two numbers.
- multiply(x, y): Return the product of two numbers.
- divide(x, y): Return the quotient or an error string on division by zero.
- modulus(x, y): Return the remainder of division.
- power(x, y): Return x raised to the power y.
- calculator(): Interactive CLI for selecting and running operations.
"""


def add(x, y):
    """Return the sum of x and y."""
    return x + y

def subtract(x, y):
    """Return the difference when y is subtracted from x."""
    return x - y

def multiply(x, y):
    """Return the product of x and y."""
    return x * y

def divide(x, y):
    """Return x / y or an error message if y is zero."""
    if y == 0:
        return "Error: Division by zero"
    return x / y

def modulus(x, y):
    """Return the remainder of x divided by y."""
    return x % y

def power(x, y):
    """Return x raised to the power y."""
    return x ** y

def calculator():
    """A simple interactive command-line calculator."""
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Power")

    choice = input("Enter choice (1-6): ")

    if choice not in ['1', '2', '3', '4', '5', '6']:
        print("Invalid input")
        return

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    elif choice == '5':
        print("Result:", modulus(num1, num2))
    elif choice == '6':
        print("Result:", power(num1, num2))

if __name__ == "__main__":
    calculator()
