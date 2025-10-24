def calculator(a, b, o):
    if o in ('add', '+'):
        return a + b
    elif o in ('subtract', '-'):
        return a - b
    elif o in ('multiply', '*'):
        return a * b
    elif o in ('divide', '/'):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"

print("Welcome to the Calculator!")

while True:
    try:
        a = float(input("What's your first number?: "))
        b = float(input("What's your second number?: "))
        o = input("What operator would you like to use? (+, -, *, /): ").strip().lower()
        result = calculator(a, b, o)
        print("Answer:", result)
    except ValueError:
        print("Invalid input. Please enter numbers only.")
    
    cont = input("Type 'exit' to quit or press Enter to continue: ").strip().lower()
    if cont == 'exit':
        print("Goodbye!")
        break