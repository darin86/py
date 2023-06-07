def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def calculator():
    print("Welcome to the Calculator!")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    operation = input("Enter the operation number (1-4): ")

    if operation not in ['1', '2', '3', '4']:
        print("Invalid operation number. Please try again.")
        return

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operation == '1':
        result = add(num1, num2)
        print(f"Result: {num1} + {num2} = {result}")
    elif operation == '2':
        result = subtract(num1, num2)
        print(f"Result: {num1} - {num2} = {result}")
    elif operation == '3':
        result = multiply(num1, num2)
        print(f"Result: {num1} * {num2} = {result}")
    elif operation == '4':
        result = divide(num1, num2)
        if isinstance(result, str):
            print(result)
        else:
            print(f"Result: {num1} / {num2} = {result}")
            
calculator()
print("Power by 黄达林")