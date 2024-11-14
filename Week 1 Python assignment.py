# Input two numbers
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
# Choose an operation
operation = input("Choose an operation (+, -, *, /): ")

# Perform the operation based on the user's input
if operation == "+":
    result = n1 + n2
    print(f"{n1} + {n2} = {result}")
elif operation == "-":
    result = n1 - n2
    print(f"{n1} - {n2} = {result}")
elif operation == "*":
    result = n1 * n2
    print(f"{n1} * {n2} = {result}")
elif operation == "/":
    if n2 != 0:
        result = n1 / n2
        print(f"{n1} / {n2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please choose +, -, *, or /.")
