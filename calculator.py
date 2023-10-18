# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Main calculator function
def calculator():
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    
    choice = input("Enter your choice: ").lower()
    
    if choice not in ('add', 'subtract', 'multiply', 'divide'):
        print("Invalid choice")
        return

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == 'add':
        result = add(num1, num2)
        print(f"Result: {num1} + {num2} = {result}")
    elif choice == 'subtract':
        result = subtract(num1, num2)
        print(f"Result: {num1} - {num2} = {result}")
    elif choice == 'multiply':
        result = multiply(num1, num2)
        print(f"Result: {num1} * {num2} = {result}")
    elif choice == 'divide':
        result = divide(num1, num2)
        print(f"Result: {num1} / {num2} = {result}")

# Run the calculator
calculator()
