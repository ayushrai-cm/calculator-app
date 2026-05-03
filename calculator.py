# =========================
#        CALCULATOR APP
# =========================

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return "❌ Error: Cannot divide by zero!" if b == 0 else a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    return "❌ Error: Cannot modulus by zero!" if b == 0 else a % b


# -------- INPUT HANDLER --------
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input! Enter a valid number.")


# -------- DISPLAY RESULT --------
def show_result(a, b, symbol, result):
    print("\n" + "-" * 40)
    if isinstance(result, str):
        print(result)
    else:
        a = int(a) if a.is_integer() else a
        b = int(b) if b.is_integer() else b
        result = int(result) if isinstance(result, float) and result.is_integer() else result
        print(f"{a} {symbol} {b} = {result}")
    print("-" * 40)


# -------- MAIN PROGRAM --------
def main():
    print("=" * 45)
    print("        🧮 CALCULATOR APP")
    print("        Simple & Clean Version")
    print("=" * 45)

    operations = {
        "1": ("Addition", "+", add),
        "2": ("Subtraction", "-", subtract),
        "3": ("Multiplication", "×", multiply),
        "4": ("Division", "÷", divide),
        "5": ("Power", "^", power),
        "6": ("Modulus", "%", modulus),
    }

    while True:
        print("\n📌 Select Operation:")
        for key, (name, symbol, _) in operations.items():
            print(f"  {key}. {name} ({symbol})")
        print("  7. Exit")

        choice = input("\nEnter choice (1-7): ").strip()

        if choice == "7":
            print("\n👋 Thank you for using Calculator App!")
            break

        if choice not in operations:
            print("❌ Invalid choice!")
            continue

        name, symbol, func = operations[choice]

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        result = func(num1, num2)
        show_result(num1, num2, symbol, result)


# -------- RUN --------
if __name__ == "__main__":
    main()
