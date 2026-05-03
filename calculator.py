def add(a, b):        return a + b
def subtract(a, b):   return a - b
def multiply(a, b):   return a * b
def divide(a, b):
    if b == 0:
        return "❌ Error: Cannot divide by zero!"
    return a / b
def power(a, b):      return a ** b
def modulus(a, b):
    if b == 0:
        return "❌ Error: Cannot modulus by zero!"
    return a % b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

def main():
    print("=" * 45)
    print("         🧮 CALCULATOR APP")
    print("         Made by Arindam Pal")
    print("=" * 45)

    operations = {
        '1': ('Addition',       '+', add),
        '2': ('Subtraction',    '-', subtract),
        '3': ('Multiplication', '×', multiply),
        '4': ('Division',       '÷', divide),
        '5': ('Power',          '^', power),
        '6': ('Modulus',        '%', modulus),
    }

    while True:
        print("\n📌 Select Operation:")
        for key, (name, symbol, _) in operations.items():
            print(f"   {key}. {name} ({symbol})")
        print("   7. Exit")

        choice = input("\nEnter choice (1-7): ").strip()

        if choice == '7':
            print("\n👋 Thank you for using Calculator App!")
            print("   Made by Arindam Pal | Chitkara University")
            break

        if choice not in operations:
            print("❌ Invalid choice! Please select 1-7.")
            continue

        name, symbol, func = operations[choice]

        num1 = get_number(f"\nEnter first number:  ")
        num2 = get_number(f"Enter second number: ")

        result = func(num1, num2)

        print("\n" + "-" * 45)
        if isinstance(result, str):
            print(f"  {result}")
        else:
            # Format nicely: remove .0 for whole numbers
            n1 = int(num1) if num1 == int(num1) else num1
            n2 = int(num2) if num2 == int(num2) else num2
            res = int(result) if isinstance(result, float) and result == int(result) else result
            print(f"  {n1} {symbol} {n2} = {res}")
        print("-" * 45)

        cont = input("\nCalculate again? (y/n): ").strip().lower()
        if cont != 'y':
            print("\n👋 Thank you for using Calculator App!")
            print("   Made by Arindam Pal | Chitkara University")
            break

if __name__ == "__main__":
    main()
