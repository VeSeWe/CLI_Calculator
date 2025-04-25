"""
This is a project for a simple
client line calculator
"""
__author__= "VeSeWe Dev"
__version__= 1.0


def calculate(op: str, x: float, y: float) -> float:
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b if b != 0 else (_ for _ in ()).throw(ZeroDivisionError("Cannot divide by zero"))
    }
    if op not in operations:
        raise ValueError("Unsupported operation.")
    return operations[op](x, y)

def parse_input(user_input):
    parts = user_input.strip().lower().split()

    word_to_symbol = {'add': '+', 'subtract': '-', 'multiply': '*', 'divide': '/'}
    if len(parts) == 3:
        if parts[1] in ['+', '-', '*', '/']:  # 2 + 3
            return parts[1], float(parts[0]), float(parts[2])
        elif parts[0] in word_to_symbol:  # add 2 3
            return word_to_symbol[parts[0]], float(parts[1]), float(parts[2])
    raise ValueError("Input should be in the form: 'add 2 3' or '2 + 3'.")

def show_help():
    print("""
Commands:
- Examples: 2 + 3 | add 2 3 | subtract 5 2 | multiply 4 2 | divide 6 3
- 'help' shows this message
- 'exit' or 'quit' to leave
""")

def main():
    print("🧮 Welcome to the Calculator!")
    show_help()

    while True:
        user_input = input("\nEnter calculation: ").strip()
        if user_input.lower() in {'exit', 'quit'}:
            print("👋 Goodbye!")
            break
        if user_input.lower() == 'help':
            show_help()
            continue

        try:
            op, x, y = parse_input(user_input)
            result = calculate(op, x, y)
            print(f"✅ Result: {result}")
        except Exception as e:
            print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    main()
