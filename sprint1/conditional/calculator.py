if __name__ == "__main__":
    a,b = map(int,input("Enter two numbers: ").split())
    op = input("Enter the operation (+, -, *, /): ")
    if op == '+':
        print(f"The sum of {a} and {b} is: {a + b}")
    elif op == '-':
        print(f"The difference of {a} and {b} is: {a - b}")
    elif op == '*':
        print(f"The product of {a} and {b} is: {a * b}")
    elif op == '/':
        if b != 0:
            print(f"The quotient of {a} and {b} is: {a / b}")
        else:
            print("Error: Division by zero is not allowed.")
    elif op == '%':
        if b != 0:
            print(f"The remainder of {a} divided by {b} is: {a % b}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation. Please enter one of +, -, *, /,%")