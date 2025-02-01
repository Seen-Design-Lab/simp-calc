def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

if __name__ == "__main__":
    import sys
    operation = sys.argv[1]
    num1 = float(sys.argv[2])
    num2 = float(sys.argv[3])

    if operation == 'add':
        print(add(num1, num2))
    elif operation == 'subtract':
        print(subtract(num1, num2))
    elif operation == 'multiply':
        print(multiply(num1, num2))
    elif operation == 'divide':
        print(divide(num1, num2))
    else:
        print("Invalid operation")